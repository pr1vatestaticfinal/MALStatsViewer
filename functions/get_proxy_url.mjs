export async function onRequest(context) {
  const proxyURL = context.env.PROXY_SERVER_URL;

  return new Response(proxyURL, {
    status: 200,
    headers: {"Content-Type": "text/plain"},
  });
}