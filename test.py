"""Just testing to retrieve data from MAL, this file will be deleted."""

from get_auth_code import build_url, get_authorization_code
from get_access_token import get_tokens
from get_api_data import get_username

url, code_challenge = build_url()

redirect_url = input("enter redirect url: ")
authorization_code = get_authorization_code(redirect_url)

if not authorization_code:
    print("authorization failed")
    exit()

response = get_tokens(authorization_code, code_challenge)
print(response)

print("Welcome, " + get_username(response.get("access_token")))
