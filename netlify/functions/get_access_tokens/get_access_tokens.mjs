import { getTokens } from "../../../access_token_helpers";

export async function handler(event) {
  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: "method not allowed"})
    };
  }

  const { code, code_verifier } = JSON.parse(event.body);

  if (!code || !code_verifier) {
    return {
      statusCode: 400,
      body: JSON.stringify({ error: "missing authorization code or code verifier"})
    };
  }

  const tokens = await getTokens(code, code_verifier);

  if (tokens.error) {
    return {
      statusCode: 500,
      body: JSON.stringify(tokens)
    };
  }

  return {
    statusCode: 200,
    body: JSON.stringify(tokens)
  };
}
