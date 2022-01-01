import json
from api.chainInfo.functions.getLocalCurrency import getLocalCurrency
from api.chainInfo.functions.getCoinPrice import getCoinPrice
from api.chainInfo.functions.getGasPrices import getGasPrices
from api.chainInfo.functions.getExchange import getExchangeRate


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
        exchange_rate = getExchangeRate(local_currency['local_currency_code'])
        # 6 generate all local currency values

        # Create prediction

        data = {
            "message": "Successful",
            "coin": body['coin'],
            "token_price": token_price,
            "local_currency": local_currency['local_currency'],
            "currency_symbol": local_currency['currency_symbol'],
            "exchange_rate": exchange_rate,
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
