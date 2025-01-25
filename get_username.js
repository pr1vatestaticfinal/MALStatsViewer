async function getAccessToken() {
    const cookies = document.cookie.split("; ");
    const tokenCookie = cookies.find(cookie => cookie.startsWith("access_token="));
    if (tokenCookie) {
        return tokenCookie.split("=")[1];
    }
    return null;
}

async function getUsername(context) {
    const PROXY_SERVER_URL = context.env.PROXY_SERVER_URL; //IMPORT VARIABLE FOR PROXY SERVER URL
    const accessToken = await getAccessToken();

    if (accessToken == null) {
        return "null";
    }

    try {
        const response = await fetch(`${PROXY_SERVER_URL}/proxy/users/@me`, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${accessToken}`,
                "Content-Type": "application/json"
            }
        });

        if (!response.ok) {
            const errorMessage = await response.text();
            console.error(`HTTPError: ${response.status}, ${errorMessage}`);
            return `HTTPError: ${response.status}, ${errorMessage}`;
        }
        const responseData = await response.json();
        const username = responseData.name || "Error: username not found";
        return username;

    } catch (error) {
        console.error(`Error: ${error.message}`);
        return `Error: ${error.message}`;
    }
}

export { getUsername };