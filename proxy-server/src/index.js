/**
 * Welcome to Cloudflare Workers! This is your first worker.
 *
 * - Run `npm run dev` in your terminal to start a development server
 * - Open a browser tab at http://localhost:8787/ to see your worker in action
 * - Run `npm run deploy` to publish your worker
 *
 * Learn more at https://developers.cloudflare.com/workers/
 */

/*export default {
	async fetch(request, env, ctx) {
		return new Response('Hello World!');
	},
};
*/

export default {
	async fetch(request, env) {
		const url = new URL(request.url);
		const PROXY_SERVER_URL = env.PROXY_SERVER_URL
		const path = url.pathname.replace(PROXY_SERVER_URL, "");
		console.log(path); //debugging
		const apiUrl = `https://api.myanimelist.net/v2${path}`;

		const origin = request.headers.get("Origin") || "https://malstatsviewer.pages.dev";

		const cookieHeader = request.headers.get("Cookie") || "";
		const tokenMatch = cookieHeader.match(/access_token=([^;]+)/);
		const accessToken = tokenMatch ? decodeURIComponent(tokenMatch[1]) : null;

		if (request.method === "OPTIONS") {
			return new Response(null, {
				status: 204,
				headers: {
					"Access-Control-Allow-Origin": origin,
					"Access-Control-Allow-Methods": "GET, OPTIONS",
					"Access-Control-Allow-Headers": "Content-Type, Authorization",
					"Access-Control-Allow-Credentials": "true"
				},
			});
		}

		if (!accessToken) {
			return new Response("Missing authorization header", {
				status: 401,
				headers: {
					"Access-Control-Allow-Origin": origin,
					"Access-Control-Allow-Credentials": "true",
				},
			});
		}

		try {
			const response = await fetch(apiUrl, {
				method: request.method,
				headers: {
					"Authorization": accessToken,
					"Content-Type": "application/json",
					"Accept": "application/json",
				},
			});

			const responseBody = await response.text();
			return new Response(responseBody, {
				status: response.status,
				headers: {
					"Content-Type": "application/json",
					"Access-Control-Allow-Origin": origin,
					"Access-Control-Allow-Credentials": "true",
				},
			});
		} catch (error) {
			return new Response(`Error: ${error.message}`, {
				status: 500,
				headers: {
					"Access-Control-Allow-Origin": origin,
					"Access-Control-Allow-Credentials": "true",
				},
			});
		}
	},
};