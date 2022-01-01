import json


def main(event, context):
    try:
        body = {
            "message": "Go Serverless v1.0! Your function executed successfully!",
        }

        return {
            "statusCode": 200,
            "body": json.dumps(body)
        }
    except:
        return {
            "statusCode": 500,
            "body": "An error occured"
        }
