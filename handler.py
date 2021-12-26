import json


def hello(event, context):
    body = {
        "message": "This is some test data for the good folks on React",
        "data": {
            "coin": "ETH | SOL",
            "dollar": 39399,
            "local_currency": "naira",
            "local_currency_price": 98989897,
            "gas_price_dollar_high": 79,
            "gas_price_local_high": 30000,
            "gas_price_dollar_mid": 30,
            "gas_price_local_mid": 150900,
            "gas_price_dollar_low": 10,
            "gas_price_local": 5799,
            "greed_fear": "Fear | Greed",
            "prediction": "Up | Down",
            "currency_symbol": "₦"
        },
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
