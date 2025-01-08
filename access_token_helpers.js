const BASE_URL = "https://myanimelist.net/v1/oauth2/token";


async function getTokens(context, code, codeVerifier) {
    const CLIENT_ID = context.env.CLIENT_ID;
    const CLIENT_SECRET = context.env.CLIENT_SECRET;

    const data = {
        client_id: CLIENT_ID,
        client_secret: CLIENT_SECRET,
        code: code,
        code_verifier: codeVerifier,
        grant_type: "authorization_code"
    }

    try {
        const response = await fetch(BASE_URL, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams(data)
        })

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`HTTP Error ${response.status}: ${errorText}`);
        }

        return await response.json();
    }
    catch (error) {
        console.error("Error fetching tokens: ", error);
        return { error: error.message };
    }
}


async function refreshToken(context, refreshToken) {
    const CLIENT_ID = context.env.CLIENT_ID;
    const CLIENT_SECRET = context.env.CLIENT_SECRET;
    
    const data = {
        client_id: CLIENT_ID,
        client_secret: CLIENT_SECRET,
        refresh_token: refreshToken,
        grant_type: "refresh_token"
    }

    try {
        const response = await fetch(BASE_URL, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams(data)
        })

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`HTTP Error ${response.status}: ${errorText}`);
        }

        return await response.json();
    }
    catch (error) {
        console.error("Error refreshing tokens: ", error);
        return { error: error.message };
    }
}


export { getTokens, refreshToken };
