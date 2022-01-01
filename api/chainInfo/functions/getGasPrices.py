import requests


def convert_Gwei_To_USD(gas, token_price, min_gas_fee):
    return ((gas / 10) * min_gas_fee * token_price) / 1000000000


def getGasPrices(token_price):
    # 1 get the current prices from ethGaasStation
    # 2 Claculate price of the (eth gas price * 21000 * token price) /10000000
    api = 'https://ethgasstation.info/api/ethgasAPI.json'

    min_fee = 21000
    response = requests.get(api)

    res_data = response.json()

    safe_low = (res_data['safeLow'], min_fee, token_price)

    average = convert_Gwei_To_USD(res_data['average'], min_fee, token_price)

    fast = convert_Gwei_To_USD(res_data['fast'], min_fee, token_price)

    return {
        'safe_low': safe_low,
        'average': average,
        'fast': fast
    }
