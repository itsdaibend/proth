import os
from dotenv import load_dotenv

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


load_dotenv()
TELEGRAM_BOT_KEY = os.environ.get('TELEGRAM_BOT_KEY')

bot = Bot(token=TELEGRAM_BOT_KEY)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_chat(message):
    await message.answer( f'<b>Welcome, {message.from_user.first_name}!</b>', parse_mode='html')

executor.start_polling(dp, skip_updates=True)