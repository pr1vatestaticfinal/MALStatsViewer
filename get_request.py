"""Module is for gaining an Authorization Code to obtain an Access Token for the user."""

import secrets
import random
import urllib.parse
from env_loader import CLIENT_ID

BASE_URL = "https://myanimelist.net/v1/oauth2/authorize" # GET REQUEST
redirect_uri = "" # OPTIONAL
code_challenge_method = "" # OPTIONAL


def build_url() -> tuple[str, str]:
    """Builds GET request URL"""
    code_challenge = generate_code_challenge()

    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "code_challenge": code_challenge,
        "state": generate_state(),
        "redirect_uri": redirect_uri if redirect_uri else None,
        "code_challenge_method": code_challenge_method
    }

    params = {k: v for k, v in params.items() if v is not None}

    query_string = urllib.parse.urlencode(params)

    get_req = BASE_URL + "?" + query_string
    print("visit url to authorize: " + get_req)

    return get_req, code_challenge


def generate_code_challenge() -> str:
    """Generates code challenge"""

    return secrets.token_urlsafe(100)[:128]


def generate_state() -> str:
    """Generates state"""

    return "RequestID" + random.randrange(0, 100)
