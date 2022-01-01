import json
from api.chainInfo.functions.getLocalCurrency import getLocalCurrency
from api.chainInfo.functions.getCoinPrice import getCoinPrice
from api.chainInfo.functions.getGasPrices import getGasPrices

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
        body = {}

        try:
            body = json.loads(event['body'])
        except:
            raise Exception("An error occured")
        # Get local Currency
        local_currency = getLocalCurrency(
            body["location"],   event["requestContext"]["identity"]["sourceIp"])
        # 2 Get token Price
        token_price = getCoinPrice(body['coin'])

        # 4 Get gas Prices
        gas_prices = getGasPrices(token_price)

        # 5 Get exchange rate

        # 6 generate all local currency values

        # Create prediction

        data = {
            "message": "Successful",
            "coin": body['coin'],
            "token_price": token_price,
            "local_currency": local_currency['local_currency'],
            "currency_symbol": local_currency['currency_symbol'],
            "gas_price_dollar_high": gas_prices['fast'],
            "gas_price_local_high": 30000,
            "gas_price_dollar_mid": gas_prices['average'],
            "gas_price_local_mid": 150900,
            "gas_price_dollar_low": gas_prices['safe_low'],
            "gas_price_local_low": 5799,
            "currency": local_currency,
            "token": token_price,
            "gas_prices": gas_prices['gasPricesGwei']
        }

        return {
            "statusCode": 200,
            "body": json.dumps(data),
        }
    except:
        return {
            "statusCode": 500,
            "body": "An error occured"
        }
