async function welcomeMessage() {
    const PROXY_SERVER_URL = await fetch("/get_proxy_url", {
        method: "get",
        mode: "cors",
        credentials: "include",
    }).then(res=>res.text());

    try {
        const response = await fetch(`${PROXY_SERVER_URL}/users/@me`, {
            method: "GET",
            mode: "cors",
            credentials: "include",
            headers: {
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

export { welcomeMessage };