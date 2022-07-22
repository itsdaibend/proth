import os
from dotenv import load_dotenv
import telebot
import requests

load_dotenv()
TELEGRAM_BOT_KEY = os.environ.get('TELEGRAM_BOT_KEY')
bot = telebot.TeleBot(TELEGRAM_BOT_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'<b>Welcome, {message.from_user.first_name}!</b>', parse_mode='html')

@bot.message_handler(commands=['phrases'])
def phrases(message):
    response = requests.get('http://localhost:8000/api/v1/languages/phrases', auth=('itsdaibend', '1@qWaSzX'))
    for entity in response.json():
        bot.send_message(message.chat.id, f'{entity["source_text"]} >>> {entity["target_text"]}', parse_mode='html')

bot.polling(none_stop=True)