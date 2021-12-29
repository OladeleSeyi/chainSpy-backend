from api.chainInfo.functions.getLocalCurrency import getLocalCurrency
import json


def main(event, context):
    body = {}

    try:
        body = json.loads(event['body'])
    except:
        exit

    data = {
        "message": "This is sample data for development",
        "currencies": getLocalCurrency(body["location"],   event["requestContext"]["identity"]["sourceIp"]),
        "event": event
    }

    return {
        "statusCode": 200,
        "body": json.dumps(data),
    }
