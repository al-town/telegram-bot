import requests
import json
from config import keys, keys_en


def get_key(d, value):  # function for beautiful output in English
    for k, v in d.items():
        if v == value:
            return k


class APIException(Exception):
    pass


class CryptoConvert:
    @staticmethod
    def get_price(value):
        if len(value) != 3:
            raise APIException('Invalid input. Wrong number of parameters (need three)')

        quote1, base1, amount = value

        try:
            quote = quote1.lower()
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Invalid input in first currency "{quote1}"')

        try:
            base = base1.lower()
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Invalid input in second currency "{base1}"')

        if quote == base:
            raise APIException('Invalid input. Convertible currencies match')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Invalid input. The "{amount}" is not a number')

        res = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        text = json.loads(res.content)[keys[base]] * amount
        quote, base = get_key(keys_en, keys[quote]), get_key(keys_en, keys[base])
        mess = f'There is {text} {base} in {amount} {quote}'
        return mess
