# coding: utf-8
import config
import requests
import pprint

api_params = {
    'apikey': config.coinwarz_api_key,
    'algo': 'lyra2rev2',
    'lyra2rev2HashRate': 1000,
    'lyra2rev2Power': 0,
    'lyra2rev2PowerCost': 0
}
COINWARZ_API_URL = 'http://www.coinwarz.com/v1/api/profitability/'

def get_json():
    return requests.get(COINWARZ_API_URL, params=api_params).json()

def write_json():
    with open('json.json', 'w') as f:
        f.write(pprint.pformat(get_json()))
