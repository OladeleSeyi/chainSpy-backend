import json

from api.chainInfo.functions.getExchange import getExchangeRate


def main(event, context):
    exchange_rate = getExchangeRate("AED")
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
