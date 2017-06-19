# coding: utf-8
import requests
from bs4 import BeautifulSoup

payload = {
    # hashrate, MH/s
    'h': 1000,
    # power (watts)
    'p': 0,
    # power cost
    'pc': 0,
    # pool fees (percent)
    'pf': 1,
    # hardware cost
    'hc': 0,

    # todo: take params from coinwarz API
    # Difficulty
    'd': 5714.15501080,
    # block reward
    'r': 50,
    # VTC/BTC
    'er': 0.00032400,
    # bitcoin cost (usd):
    'btcer': 2550.18000000
}
url = 'https://www.coinwarz.com/calculators/vertcoin-mining-calculator/'

def get_daily_profits_btc():
    r = requests.get(url, params=payload)
    parsed = BeautifulSoup(r.text, 'html.parser')
    daily_profits = parsed.select('table.table.table-hover > tbody > tr:nth-of-type(2) > td:nth-of-type(3)')[0].text.strip()
    return daily_profits
