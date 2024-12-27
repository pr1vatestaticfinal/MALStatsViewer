"""Gets authorization code and code challenge"""

import get_auth_code
import json


def handler(event, context):
    try:
        auth_url, code_challenge = get_auth_code.build_url()
        return {
            "statusCode": 200,
            "body": json.dumps({
                "auth_url": auth_url,
                "code_challenge": code_challenge
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
