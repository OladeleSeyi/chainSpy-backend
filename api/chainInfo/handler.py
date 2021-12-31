import json

from api.chainInfo.functions.getLocalCurrencyValue import getLocalCurrencyValue


def main(event, context):

    local_currency_value = getLocalCurrencyValue(4, 4500)
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "local_currency_value": local_currency_value
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
