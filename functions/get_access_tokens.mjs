import { getTokens } from "../access_token_helpers";

export async function onRequest(context) {
  const request = context.request;

  if (request.method !== "POST") {
    return new Response(
      JSON.stringify({ error: "method not allowed" }),
      { status: 405, headers: { "Content-Type": "application/json" } }
    );
  }

  const { code, code_verifier } = await request.json();

  if (!code || !code_verifier) {
    return new Response(
      JSON.stringify({ error: "missing authorization code or code verifier" }),
      { status: 400, headers: { "Content-Type": "application/json" } }
    );
  }

  const tokens = await getTokens(context, code, code_verifier);

  if (tokens.error) {
    return new Response(
      JSON.stringify(tokens),
      { status: 500, headers: { "Content-Type": "application/json" } }
    );
  }

  return new Response(
    JSON.stringify(tokens),
    { status: 200, headers: { "Content-Type": "application/json" } }
  );
}