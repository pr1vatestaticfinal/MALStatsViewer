from flask import Flask, render_template
import secrets
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CLIENT_ID = os.environ.get("CLIENT_ID")
BASE_URL = "https://myanimelist.net/v1/oauth2/authorize"

@app.route('/')
def index():
    def get_new_code_verifier() -> str:
        token = secrets.token_urlsafe(100)
        return token[:128]

    code_challenge = get_new_code_verifier()

    url = f"{BASE_URL}?response_type=code&client_id={CLIENT_ID}&code_challenge={code_challenge}"

    return render_template('index.html', auth_url=url)

if __name__ == '__main__':
    app.run(debug=True)