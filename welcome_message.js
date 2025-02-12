async function getAccessToken() {
    const cookies = document.cookie.split("; ");
    const tokenCookie = cookies.find(cookie => cookie.startsWith("access_token="));
    if (tokenCookie) {
        return tokenCookie.split("=")[1];
    }
    return null;
}

async function welcomeMessage() {
    const accessToken = await getAccessToken();

    try {
        const response = await fetch("/proxy/users/@me?fields=username", {
            headers: {
                "Authorization": `Bearer ${accessToken}`,
                "Content-Type": "application/json"
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);

        }

        const responseData = await response.json();
        const username = responseData.username || "null";

        document.querySelector(".welcome").textContent = `Welcome, ${username}`;
    } catch (error) {
        console.error("Error fetching username:", error);
        document.querySelector(".welcome").textContent = "Welcome, null";
    }
}

export { welcomeMessage }