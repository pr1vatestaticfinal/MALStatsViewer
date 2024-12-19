"""Module is for gaining an Authorization Code to obtain an Access Token for the user."""

import secrets
import random
import urllib.parse
from env_loader import CLIENT_ID

BASE_URL = "https://myanimelist.net/v1/oauth2/authorize" # GET REQUEST
redirect_uri = "" # OPTIONAL
code_challenge_method = "plain" # OPTIONAL


def build_url() -> tuple[str, str]:
    """Builds GET request URL. Returns tuple containing authenticator URL and code verifier."""
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


def get_authorization_code(redirect_url: str) -> str | None:
    """Collects authorization code from direct URL. If no authorization code is found, None is returned."""
    parsed_url = urllib.parse.urlparse(redirect_url)
    authorization_code = urllib.parse.parse_qs(parsed_url.query).get("code", [None])[0]

    return authorization_code


def generate_code_challenge() -> str:
    """Generates code challenge"""

    return secrets.token_urlsafe(100)[:128]


def generate_state() -> str:
    """Generates state"""

    return "RequestID" + str(random.randrange(0, 100))
