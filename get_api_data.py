"""This module retrieves data from the MAL API using an access token"""

import urllib.request
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