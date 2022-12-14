import aiohttp

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from states import AuthenticationGroup
from config import TELEGRAM_BOT_KEY


bot = Bot(token=TELEGRAM_BOT_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_chat(message: types.Message):
    kb = [
        [types.KeyboardButton(text="How to use this bot?")],
        [types.KeyboardButton(text="List of my words")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer( f'<b>Welcome, {message.from_user.first_name}!</b>', parse_mode='html', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "How to use this bot?")
async def how_to_use_this_bot(message: types.Message):
    await message.reply("For now, you can learn new words in different languages by translating them.\n\nFirstly, you have to visit our site and register there.\nSecondly, you should authenticate pressing the Authenticate button in bot.\nAfter that, you can use our bot.")

@dp.message_handler(commands=['auth'], state=None)
async def enter_auth(message: types.Message):
    await message.answer('Enter your username on Proth website:')
    await AuthenticationGroup.username.set()
    
@dp.message_handler(state=AuthenticationGroup.username)
async def get_first_auth_answer(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(username=answer)
    await message.answer('Enter your password on Proth website:')
    await AuthenticationGroup.next()
    
@dp.message_handler(state=AuthenticationGroup.password)
async def get_second_auth_answer(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(password=answer)
    
    data = await state.get_data()
    await message.answer(f"Your username - {data.get('username')}, password - {data.get('password')}")
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.post('http://localhost:8000/api/v1/token/', data=data) as resp:
            assert resp.status == 200
            refresh_token = await resp.text()
            # вероятно надо сделать state для refresh token
    
    await state.finish()

@dp.message_handler(lambda message: message.text == "List of my words")
async def list_of_words(message: types.Message):
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get('http://localhost:8000/api/v1/token/') as resp:
            print(resp.status)
    await message.reply(await resp.text())

executor.start_polling(dp, skip_updates=True)