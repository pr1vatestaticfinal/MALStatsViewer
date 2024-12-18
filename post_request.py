"""Module for obtaining a user's Access Token."""

import os
import urllib.error
import urllib.request
import urllib.parse
import json

BASE_URL = "https://myanimelist.net/v1/oauth2/token"


def get_response(code: str, code_verifier: str) -> dict:
    """Sends a POST Request to obtain an Access Token.
    Returns response in dictionary format (JSON parsed)."""

    data = {
        "client_id": os.environ.get("CLIENT_ID"),
        "client_secret": os.environ.get("CLIENT_SECRET"),
        "code": code,
        "code_verifier": code_verifier,
        "grant_type": "authorization_code"
    }

    encoded_data = urllib.parse.urlencode(data).encode("utf-8")

    req = urllib.request.Request(BASE_URL, data=encoded_data, method="POST")

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
        return {"error": error_message}
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": str(e)}
