export async function onRequest(context) {
  const proxyURL = context.env.PROXY_SERVER_URL;

  return new Response(proxyURL, {
    status: 200,
    headers: {
      "Content-Type": "text/plain",
      "Access-Control-Allow-Origin": "https://malstatsviewer.pages.dev",
			"Access-Control-Allow-Methods": "GET, OPTIONS",
			"Access-Control-Allow-Headers": "Content-Type, Authorization",
    },
  });
}