export async function onRequest(context) {
    return context.env.PROXY_SERVER_URL;
  }