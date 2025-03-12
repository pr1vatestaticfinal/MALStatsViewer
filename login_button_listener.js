document.getElementById("dynamic-link").addEventListener("click", async(event) => {
    event.preventDefault();

    try {
        const response = await fetch("/get_auth_code");

        if (!response.ok) {
            throw new Error("failed to fetch auth URL");
        }

        const data = await response.json()
        const authURL = data.auth_url;
        const codeChallenge = data.code_challenge;

        const expiryDate = new Date();
        expiryDate.setTime(expiryDate.getTime() + (10 * 60 * 1000));

        document.cookie = `code_challenge=${encodeURIComponent(codeChallenge)}; expires=${expiryDate.toUTCString()}; path=/; secure`;

        window.location.href = authURL;
    }

    catch (error) {
        console.error("Error: ", error)
    }
})