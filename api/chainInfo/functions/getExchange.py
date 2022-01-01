import requests
import os
import json

access_key = os.environ['exchangeRateKey']


def getExchangeRate(currency):
    query = {
        'app_id': access_key,
    }
    response = {}
    try:
        response = requests.get(
            "https://openexchangerates.org/api/latest.json", params=query)
    except:
        raise Exception("An error occured getting exchange rates")
    res_data = response.json()

    rate = res_data['rates'][currency]

    return rate
