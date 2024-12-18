"""Module for creating GET request for MAL's API."""

import secrets
import random
import os
from dotenv import load_dotenv

BASE_URL = "https://myanimelist.net/v1/oauth2/authorize" # GET REQUEST
redirect_uri = "" # OPTIONAL
code_challenge_method = "" # OPTIONAL


def build_url() -> str:
    """Builds GET request URL"""
    load_dotenv()

    return BASE_URL + f"?response_type:code&client_id={os.environ.get("CLIENT_ID")}&code_challenge={generate_code_challenge()}&state={generate_state()}"


def generate_code_challenge() -> str:
    """Generates code challenge"""

    return secrets.token_urlsafe(100)[:128]


def generate_state() -> str:
    """Generates state"""

    return "RequestID" + random.randrange(0, 100)
