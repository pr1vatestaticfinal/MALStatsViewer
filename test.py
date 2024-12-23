"""Just testing to retrieve data from MAL, this file will be deleted."""

from get_auth_code import build_url, get_authorization_code
from get_access_token import get_tokens
from get_api_data import get_username, get_user_anime_list, get_img_url, get_title, get_updated_at_date, get_user_score

url, code_challenge = build_url()

redirect_url = input("enter redirect url: ")
authorization_code = get_authorization_code(redirect_url)

if not authorization_code:
    print("authorization failed")
    exit()

response = get_tokens(authorization_code, code_challenge)
print(response)

print("Welcome, " + get_username(response.get("access_token")))

anime_list_data = get_user_anime_list(response.get("access_token"))

print("User anime list: ")
print(anime_list_data)

anime_list_iter = iter(anime_list_data.get("data"))
silly_data = next(anime_list_iter)

print(silly_data)

print("silly data: ")
print(get_user_score(silly_data))
print(get_img_url(silly_data))
print(get_title(silly_data))
print(get_updated_at_date(silly_data))
