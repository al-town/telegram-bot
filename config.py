TOKEN = 'token of telegram bot'

# dictionaries with values of available currencies
keys = {'биткоин': 'BTC', 'эфириум': 'ETH', 'рубль': 'RUB', 'евро': 'EUR', 'доллар': 'USD',
        'bitcoin': 'BTC', 'ethereum': 'ETH', 'ruble': 'RUB', 'euro': 'EUR', 'dollar': 'USD'}
keys_en = {'bitcoin': 'BTC', 'ethereum': 'ETH', 'ruble': 'RUB', 'euro': 'EUR', 'dollar': 'USD'}

start_message = "I'm Currency Converter Bot.\n" \
                "I can work with russian and english currency names, but I only speak english. " \
                "I'm no case sensitive. \n" \
                "Use /help to learn how to use me.\n" \
                "Use /values to see a list of available currencies.\n" \
                "API is provided by cryptocompare.com"

help_message = 'To get started, enter the bot command in the following format: '\
                '\n <currency name>'\
                '\n <what currency to transfer>'\
                '\n <the amount of the transferred currency>'\
                '\nIn one line, using space as separator, use "." for float amount.'\
                '\nUse /values to see a list of available currencies'
