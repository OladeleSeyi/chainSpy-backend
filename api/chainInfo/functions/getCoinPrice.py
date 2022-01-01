from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

access_key = os.environ['coinMCapKey']


def getCoinPrice(coin):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    query = {
        'symbol': coin
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': access_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=query)
        res_data = response.json()
        return res_data['data'][coin]['quote']['USD']['price']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        raise Exception("An Error occured with  Price confirmation")
