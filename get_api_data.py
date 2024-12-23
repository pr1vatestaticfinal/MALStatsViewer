"""This module retrieves data from the MAL API using an access token"""

import urllib.request
import urllib.parse
import urllib.error
import json


def get_username(access_token: str) -> str:
    """Gets username associated with access token."""

    url = "https://api.myanimelist.net/v2/users/@me"

    req = urllib.request.Request(url, method="GET")
    req.add_header("Authorization", f"Bearer {access_token}")

    try:
        with urllib.request.urlopen(req) as response:
            response_data: dict = json.load(response)
            username = response_data.get("name", "Error: username not found")
            return username
        
    except urllib.error.HTTPError as e:
        error_message = e.read().decode("utf-8")
        print(f"HTTPError: {e.code}, {error_message}")
        return f"HTTPError: {e.code}, {error_message}"
    
    except urllib.error.URLError as e:
        print(f"URLError: {e.reason}")
        return f"URLError: {e.reason}"
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}"
    

def get_user_anime_list(access_token: str, offset=0) -> dict:
    """Gets anime list associated with user.
    
    Format:
    {
        "data": 
        [
            {
                "node":
                {
                    "id": 123,
                    "title": "ANIME",
                    "main_picture":
                        {
                            "medium": "url.jpg",
                            "large": "url.jpg"
                        }
                },
                "list_status":
                {
                    "status": "completed",
                    "score": 10,
                    "num_episodes_watched": 21,
                    "is_rewatching": False,
                    "updated_at": "2024-01-01..."
                }
            },

            {
                "node"...
            }
        ],
        "paging":
        {
            "next": "url.net/?query_string"
        }
    }
    """

    url = "https://api.myanimelist.net/v2/users/@me/animelist"

    params = {
        "sort": "list_score",
        "fields": "list_status",
        "offset": offset
    }

    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {access_token}")

    try:
        with urllib.request.urlopen(req) as response:
            response_data = json.load(response)
            return response_data
        
    except urllib.error.HTTPError as e:
        error_message = e.read().decode("utf-8")
        print(f"HTTPError: {e.code}, {error_message}")
        return {"error": error_message}
    
    except urllib.error.URLError as e:
        print(f"URLError: {e.reason}")
        return {"error": e.reason}
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": str(e)}
    

def get_title(list_item: dict) -> str:
    """Gets title of anime in node."""

    return list_item.get("node").get("title")


def get_img_url(list_item: dict) -> str:
    """Gets URL of image of anime in node."""
    
    return list_item.get("node").get("main_picture").get("medium", "no img")


def get_user_score(list_item: dict) -> int:
    """Gets user score of anime in list status."""

    return list_item.get("list_status").get("score", "N/A")


def get_updated_at_date(list_item: dict):
    """Gets date in which user updated anime to list."""

    return list_item.get("list_status").get("updated_at")[:10]
