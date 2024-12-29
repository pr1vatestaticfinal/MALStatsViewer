export async function handler(event) {
  const {queryStringParams} = event;

  const authCode = queryStringParams.code || null;
  const state = queryStringParams.state || null;

  if (!authCode) {
    return {
      statusCode: 400,
      body: "Authorization code not found"
    };
  }

  console.log("Authorization code: ", authCode);
  console.log("state: ", state);
}
