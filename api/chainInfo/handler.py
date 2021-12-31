import json

from api.chainInfo.functions.getCoinPrice import getCoinPrice


def main(event, context):

    getCoinPrice("SOL")
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
