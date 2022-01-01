import requests
import os
import json

access_key = os.environ['positionKey']


def getLocalCurrency(location, ip_address=None):
    query = {}

    if (isinstance(location, dict) and ('lat' and 'long') in location):
        lat = location['lat']
        long = location['long']
        print("watermellon falls")

        query = {
            'access_key': access_key,
            'query': f'{lat},{long}',
            'country_module': 1,
            'limit': 1,
        }

    else:
        query = {
            'access_key': access_key,
            'query': ip_address,
            'country_module': 1,
            'limit': 1,
        }

    response = requests.get(
        'http://api.positionstack.com/v1/reverse?', params=query)

    res_data = response.json()

    currency = res_data['data'][0]['country_module']['currencies'][0]

    return {
        "local_currency": currency['name'],
        "currency_symbol": currency['symbol'],
        "local_currency_code": currency['code']
    }
