"""OMG I CAN ACCESS THE API WITH THIS FILE"""

import secrets
import random

BASE_URL = "https://myanimelist.net/v1/oauth2/authorize" # GET REQUEST
redirect_uri = "" # OPTIONAL
code_challenge_method = "" # OPTIONAL
client_id = "" 
client_secret = ""

def build_url() -> str:
    """Builds GET request URL"""
    configure()

    return BASE_URL + f"?response_type:code&client_id={client_id}&code_challenge={generate_code_challenge()}&state={generate_state()}"


def generate_code_challenge() -> str:
    """Generates code challenge"""

    return secrets.token_urlsafe(100)[:128]


def generate_state() -> str:
    """Generates state"""

    return "RequestID" + random.randrange(0, 100)
