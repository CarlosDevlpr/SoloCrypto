from flask import Flask, request, jsonify
from requests import Request, Session
import json

app = Flask(__name__)

headers = {
    'Accepts' : 'apllication/json',
    'X-CMC_PRO_API_KEY' : '71cf5570-cc66-4a51-b05b-adcd4ed984f4'
}


def cryptoSearch(selected_crypto, selected_currency):
    url ='https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    selected_currency = selected_currency.upper()
    parameters = {
        'slug' : selected_crypto,
        'convert' : selected_currency
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    resultSearch = json.loads(response.text)['data']
    crypto_dict = resultSearch
    crypto_idd = list(resultSearch.keys())
    crypto_dict = resultSearch[crypto_idd[0]]
    crypto_name = crypto_dict['name']
    crypto_symbol = crypto_dict['symbol']
    crypto_quotes = crypto_dict['quote']
    crypto_quotes_currency = crypto_quotes[selected_currency]
    crypto_price = crypto_quotes_currency['price']
    return crypto_name, crypto_symbol ,crypto_price



app.config['SECRET_KEY'] = 'f08e6e50f2529a5c1a7dc13844f5a213'

from source import routes