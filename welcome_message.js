async function getAccessToken() {
    const cookies = document.cookie.split("; ");
    const tokenCookie = cookies.find(cookie => cookie.startsWith("access_token="));
    if (tokenCookie) {
        return tokenCookie.split("=")[1];
    }
    return null;
}

async function welcomeMessage() {
    const PROXY_SERVER_URL = await fetch("/get_proxy_url");
    const accessToken = await getAccessToken();

    try {
        const response = await fetch(`${PROXY_SERVER_URL}/users/@me`, {
            headers: {
                "Authorization": `Bearer ${accessToken}`,
                "Content-Type": "application/json"
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);

        }

        const responseData = await response.json();
        const username = responseData.name || "null";

        document.querySelector(".welcome").textContent = `Welcome, ${username}`;
    } catch (error) {
        console.error("Error fetching username:", error);
        document.querySelector(".welcome").textContent = "Welcome, null";
    }
}

export { welcomeMessage }