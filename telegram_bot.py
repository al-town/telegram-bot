import telebot
from extensions import CryptoConvert, APIException
from config import keys_en, TOKEN, help_message, start_message
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])  # decorator for start command
def start(message: telebot.types.Message):
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=['help'])  # decorator for help command
def help_(message: telebot.types.Message):
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=['values'])  # decorator for values command
def values(message: telebot.types.Message):
    text = 'Available currencies: '
    for key in keys_en.keys():
        text += f'\n {key}'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text', ])  # decorator to handle custom messages
def convert(message: telebot.types.Message):
    try:
        value = message.text.split(' ')
        text = CryptoConvert.get_price(value)
    except APIException as e:
        bot.reply_to(message, f'User error: {e}')
    except Exception as e:
        bot.reply_to(message, f'Command cannot be processed\n{e}')
    else:
        bot.send_message(message.chat.id, text)


# bot launch. The none_stop=True parameter tells the bot to try not to stop when any errors occur.
bot.polling(none_stop=True)
