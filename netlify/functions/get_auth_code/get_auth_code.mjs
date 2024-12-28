import crypto from "crypto";
import querystring from "querystring"

const CLIENT_ID = process.env.CLIENT_ID;
const BASE_URL = "https://myanimelist.net/v1/oauth2/authorize";

function generateCodeChallenge() {
  return crypto.randomBytes(100).toString("base64url").slice(0, 128)
}

function generateState() {
  return "RequestID" + Math.floor(Math.random() * 100);
}

export function buildURL() {
  const codeChallenge = generateCodeChallenge();
  const state = generateState();

  const params = {
    response_type: "code",
    client_id: CLIENT_ID,
    code_challenge: codeChallenge,
    state: state
  };

  return {
    auth_url: `${BASE_URL}?${querystring.stringify(params)}`,
    code_challenge: codeChallenge
  };
}