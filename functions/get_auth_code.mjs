import crypto from "crypto";
import querystring from "querystring";

const CLIENT_ID = process.env.CLIENT_ID;
const BASE_URL = "https://myanimelist.net/v1/oauth2/authorize";

function generateCodeChallenge() {
  return crypto.randomBytes(100).toString("base64url").slice(0, 128)
}

function generateState() {
  return "RequestID" + Math.floor(Math.random() * 100);
}

export async function handler(event, context) {
  const codeChallenge = generateCodeChallenge();
  const state = generateState();

  const params = {
    response_type: "code",
    client_id: CLIENT_ID,
    code_challenge: codeChallenge,
    state: state
  };

  const authURL = `${BASE_URL}?${querystring.stringify(params)}`;

  return {
    statusCode: 200,
    body: JSON.stringify({
      auth_url: authURL,
      code_challenge: codeChallenge
    })
  };
}