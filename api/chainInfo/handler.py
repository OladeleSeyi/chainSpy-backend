import json
#   1.  Receive and validate the request
# 2. Get the local currency
#     1. using the provided lat and longitude values get the local  currency of the user and the symbol from [PositionStack Api](https://positionstack.com/) .
#     2. if no location is provided get the local currency and symbol from the IP Address.
# 3. Get current price of the asset from CoinGecko in USD
#     1. Use the CoinGecko Api
# 4. Get gas prices from etherscan or sol scan
# 5. Convert the value with the given exchange rate.
# 6. Create a prediction based on yesterday’s price, and the prices for the past week.
# 7. Return the response.


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
