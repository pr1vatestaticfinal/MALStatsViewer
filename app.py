from flask import Flask, render_template, redirect, url_for, session, request, jsonify
import requests
import uuid
import secrets
import os
import datetime
from dotenv import load_dotenv
from collections import Counter

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
AUTH_URL = "https://myanimelist.net/v1/oauth2/authorize"
USER_URL = "https://api.myanimelist.net/v2/users/@me"
ANIME_LIST_URL = "https://api.myanimelist.net/v2/users/@me/animelist"
TOKEN_URL = "https://myanimelist.net/v1/oauth2/token"


def get_new_code_verifier() -> str:
    token = secrets.token_urlsafe(100)
    return token[:128]

def convert_timestamp(ts) -> str:
    try:
        dt = datetime.datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S+00:00")
        return dt.strftime("%B %d, %Y at %I:%M%p UTC")
    except ValueError:
        return "N/A"

app.jinja_env.filters["convert_timestamp"] = convert_timestamp

def get_anime_list_page(access_token: str, next_url: str = None) -> dict:
    headers = {"Authorization": f"Bearer {access_token}"}

    if next_url:
        response = requests.get(next_url, headers=headers)
    else:
        params = {
            "fields": "list_status,genres,title,mean,num_episodes",
            "sort": "list_updated_at",
            "limit": 100,
            "nsfw": True
        }
        response = requests.get(ANIME_LIST_URL, headers=headers, params=params)

    response.raise_for_status()
    return response.json()

def get_full_anime_list(access_token: str) -> list:
    if "full_anime_list_cache" in session:
        return session["full_anime_list_cache"]
    
    all_anime = []
    next_url = None

    try:
        data = get_anime_list_page(access_token)
        all_anime.extend(data.get("data", []))
        next_url = data.get("paging", {}).get("next")

        while next_url:
            data = get_anime_list_page(access_token, next_url)
            all_anime.extend(data.get("data", []))
            next_url = data.get("paging", {}).get("next")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching full anime list: {e}")
        return []
    
    session["full_anime_list_cache"] = all_anime
    return all_anime

def process_anime_data(anime_list: list, period: str) -> dict:
    end_date = datetime.datetime.now(datetime.timezone.utc)

    if period == "6m":
        start_date = end_date - datetime.timedelta(days=180)
    elif period == "1y":
        start_date = end_date - datetime.timedelta(days=365)
    elif period == "all":
        start_date = datetime.datetime.min.replace(tzinfo=datetime.timezone.utc)
    else:
        start_date = datetime.datetime.min.replace(tzinfo=datetime.timezone.utc)

    filtered_entries = []
    genre_counts = Counter()

    for entry in anime_list:
        try:
            ts_str = entry["list_status"]["updated_at"]
            dt = datetime.datetime.strptime(ts_str, "%Y-%m-%dT%H:%M:%S+00:00").replace(tzinfo=datetime.timezone.utc)

            if dt >= start_date:
                filtered_entries.append(entry)

                anime_info = entry.get("node", {})
                genres = anime_info.get("genres", [])
                for genre in genres:
                    genre_counts[genre["name"]] += 1
        
        except Exception:
            continue

    top_rated = sorted(
        [e for e in filtered_entries if e["list_status"]["score"] > 0],
        key=lambda x: x["list_status"]["score"],
        reverse=True
    )[:10]

    total_genre_counts = sum(genre_counts.values())
    genre_distribution = {}
    if total_genre_counts > 0:
        for genre, count in genre_counts.items():
            genre_distribution[genre] = round((count / total_genre_counts) * 100, 2)
    
    sorted_genres = dict(sorted(genre_distribution.items(), key=lambda item: item[1], reverse=True))

    return {
        "entry_count": len(filtered_entries),
        "top_rated": top_rated,
        "genre_distribution": sorted_genres
    }
        

@app.route('/')
def index():
    user_data = None
    recent_entries = []

    if "access_token" in session:
        access_token = session["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}

        try:
            user_response = requests.get(USER_URL, headers=headers)
            user_response.raise_for_status()
            user_data = user_response.json()

            params = {
                "fields": "list_status",
                "sort": "list_updated_at",
                "limit": 10,
                "nsfw": True
            }
            list_response = requests.get(ANIME_LIST_URL, headers=headers, params=params)
            list_response.raise_for_status()
            list_data = list_response.json()

            recent_entries = list_data.get("data", [])

        except requests.exceptions.RequestException as e:
            print("Authentication/API Error: {e}. Clearing session.")
            session.pop("access_token", None)
            session.pop("refresh_token", None)
            user_data = None

    return render_template("index.html", user_data=user_data, recent_entries=recent_entries)

@app.route("/data")
def get_data_for_period():
    if "access_token" not in session:
        return jsonify({"error": "User not authenticated"}), 401
    
    period = request.args.get("period", "6m") # Default to 6 months
    access_token = session["access_token"]

    try:
        full_list = get_full_anime_list(access_token)

        if not full_list:
            return jsonify({"error": "Could not fetch or access anime list data"}), 500
        
        results = process_anime_data(full_list, period)

        processed_top_rated = []
        for entry in results["top_rated"]:
            processed_top_rated.append({
                "title": entry["node"]["title"],
                "score": entry["list_status"]["score"],
                "updated_at": entry["list_status"]["updated_at"],
                "mean": entry["node"].get("mean"),
                "num_episodes": entry["node"].get("num_episodes"),
                "id": entry["node"]["id"]
            })
        
        return jsonify({
            "period": period,
            "entry_count": results["entry_count"],
            "top_rated": processed_top_rated,
            "genre_distribution": results["genre_distribution"]
        })

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            # token expired
            session.pop("access_token", None)
            session.pop("full_anime_list_cache", None)
            return jsonify({"error": f"API Error: {str(e)}"}), 500
    except Exception as e:
        print(f"Error processing data for period {period}: {e}")
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route("/login")
def login():
    state = str(uuid.uuid4())
    code_challenge = get_new_code_verifier()

    session["oauth_state"] = state
    session["code_challenge"] = code_challenge

    url = (
        f"{AUTH_URL}"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&code_challenge={code_challenge}"
        f"&state={state}"
    )

    return redirect(url)

@app.route("/callback")
def callback():
    auth_code = request.args.get("code")
    state = request.args.get("state")

    if state != session.get("oauth_state"):
        return "States don't match", 400
    
    code_challenge = session.get("code_challenge")

    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": auth_code,
        "code_verifier": code_challenge,
        "grant_type": "authorization_code"
    }

    try:
        response = requests.post(TOKEN_URL, data=data)
        response.raise_for_status()
        tokens = response.json()

        session["access_token"] = tokens["access_token"]
        session["refresh_token"] = tokens["refresh_token"]

        session.pop("oauth_state", None)
        session.pop("code_verifier", None)
        session.pop("full_anime_list_cache", None)

        return redirect(url_for("index"))
    except requests.exceptions.RequestException as e:
        print(f"Error during token exchange: {e}")
        return "Failed to get tokens", 500
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)