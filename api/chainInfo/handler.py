import json


def main(event, context):
    body = {
        "message": "This is sample data for development",
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
