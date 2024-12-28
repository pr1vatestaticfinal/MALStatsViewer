document.getElementById("dynamic-link").addEventListener("click", async(event) => {
    event.preventDefault();

    try {
        const response = await fetch("/.netlify/functions/get_auth_code")

        if (!response.ok) {
            throw new Error("failed to fetch auth URL");
        }

        const data = await response.json()
        const authURL = data.auth_url;
        const codeChallenge = data.code_challenge;

        sessionStorage.setItem("code_challenge", codeChallenge)

        window.location.href = authURL;
    }

    catch (error) {
        console.error("Error: ", error)
    }
})