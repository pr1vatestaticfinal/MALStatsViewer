const BASE_URL = "https://myanimelist.net/v1/oauth2/authorize";

function generateCodeChallenge() {
  const buffer = new Uint8Array(100);
  
  crypto.getRandomValues(buffer);
 
  let base64UrlString = btoa(String.fromCharCode.apply(null, buffer))
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=+$/, '');
 
  return base64UrlString.slice(0, 128);
}

function generateState() {
  return "RequestID" + Math.floor(Math.random() * 100);
}

export async function onRequest(context) {
  const CLIENT_ID = context.env.CLIENT_ID;

  const codeChallenge = generateCodeChallenge();
  const state = generateState();

  const params = new URLSearchParams({
    response_type: "code",
    client_id: CLIENT_ID,
    code_challenge: codeChallenge,
    state: state
  });

  const authURL = `${BASE_URL}?${params.toString()}`;

  return new Response(
    JSON.stringify({
      auth_url: authURL,
      code_challenge: codeChallenge
    }),
    {
      headers: { "Content-Type": "application/json" }
    }
  )
}