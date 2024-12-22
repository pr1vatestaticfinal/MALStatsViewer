"""Module for obtaining a user's Access Token."""

import urllib.error
import urllib.request
import urllib.parse
import json
from env_loader import CLIENT_ID, CLIENT_SECRET

BASE_URL = "https://myanimelist.net/v1/oauth2/token"


def get_tokens(code: str, code_verifier: str) -> dict:
    """Sends a POST Request to obtain an Access Token.
    Returns response in dictionary format (JSON parsed).
    Possible JSON Response:

    {
        "token_type": "Bearer",
        "expires_in": 2678400,
        "access_token": "a1b2c3...",
        "refresh_token": "z9y8x7..."
    }
    
    """

    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
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
        return {"error": e.reason}
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": str(e)}


def refresh_token(refresh_token: str):
    """Grants user new access token after the previous one expires.
    
    Possible JSON Response:

    {
        "token_type": "Bearer",
        "expires_in": 2678400,
        "access_token": "a1b2c3...",
        "refresh_token": "z9y8x7..."
    }
    
    """

    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
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
        return {"error": e.reason}
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": str(e)}
