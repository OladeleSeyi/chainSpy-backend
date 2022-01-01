import json

from api.chainInfo.functions.getGasPrices import getGasPrices


def main(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
