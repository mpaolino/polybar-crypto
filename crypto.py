#!/usr/bin/env python3

import configparser
import sys
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from decimal import Decimal
from os.path import expanduser

home = expanduser("~")
config = configparser.ConfigParser()
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# File must be opened with utf-8 explicitly
with open(f'{home}/.config/polybar/crypto-config', 'r', encoding='utf-8') as f:
	config.read_file(f)

# Everything except the general section
currencies = [x for x in config.sections() if x != 'general']
base_currency = config['general']['base_currency']
api_key = config['general']['api_key']

parameters = {
  'start':'1',
  'limit':'5000',
  'convert': base_currency
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    sys.stderr.write(e)
    exit(1)


for currency in currencies:
    icon = config[currency]['icon']
 
    local_price = None
    for coin in data['data']:
        if coin['slug'] == currency:
            local_price = round(Decimal(coin['quote'][base_currency]['price']), 2)
            change_24 = round(Decimal(coin['quote'][base_currency]['percent_change_24h']), 2)
    
    if local_price is None:
        continue

    display_opt = config['general']['display']
    if display_opt == 'both' or display_opt == None:
    	sys.stdout.write(f'{icon} {local_price}/{change_24:+}%  ')
    elif display_opt == 'percentage':
    	sys.stdout.write(f'{icon} {change_24:+}%  ')
    elif display_opt == 'price':
    	sys.stdout.write(f'{icon} {local_price}  ')
