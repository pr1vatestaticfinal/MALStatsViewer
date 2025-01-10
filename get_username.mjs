async function getAccessToken() {
    const cookies = document.cookie.split("; ");
    const tokenCookie = cookies.find(cookie => cookie.startsWith("access_token="));
    if (tokenCookie) {
        return tokenCookie.split("=")[1];
    }
    return null;
}

export async function getUsername() {
    const url = "https://api.myanimelist.net/v2/users/@me";
    const accessToken = getAccessToken()

    try {
        const response = await fetch(url, {
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

