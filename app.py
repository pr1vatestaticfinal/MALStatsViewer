from flask import Flask, render_template, redirect, url_for, session, request
import requests
import uuid
import secrets
import os
import datetime
from dotenv import load_dotenv

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


@app.route('/')
def index():
    user_data = None
    list_data = None
    animes_this_year = 0
    recent_entries = []

    if "access_token" in session:
        access_token  = session["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}

        try:
            # Gathering user and list data
            user_response = requests.get(USER_URL, headers=headers)
            user_response.raise_for_status()
            user_data = user_response.json()

            params = {
            "fields": "list_status",
            "sort": "list_updated_at",
            "limit": 10
            }

            list_response = requests.get(ANIME_LIST_URL, headers=headers, params=params)
            list_response.raise_for_status()
            list_data = list_response.json()

            print(list_data)

            if list_data and "data" in list_data:
                recent_entries = list_data["data"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching user data: {e}")
            session.pop("access_token", None)
            return redirect(url_for("index"))
        
    return render_template("index.html", user_data=user_data, recent_entries=recent_entries)
        

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