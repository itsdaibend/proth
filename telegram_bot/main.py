import aiohttp
import database

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from states import AuthenticationGroup, ExtendPhrasesGroup
from keyboards import main_keyboard, languages_keyboard
from config import TELEGRAM_BOT_KEY
from models import User


bot = Bot(token=TELEGRAM_BOT_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup():
    await database.setup()


@dp.message_handler(commands=['start'])
async def start_chat(message: types.Message):
    await message.answer(f'<b>Welcome, {message.from_user.first_name}!</b>', parse_mode='html', reply_markup=main_keyboard())


@dp.message_handler(lambda message: message.text == "How to use this bot?")
async def how_to_use_this_bot(message: types.Message):
    await message.reply("For now, you can learn new words in different languages by translating them.\n\nFirstly, you have to visit our site and register there.\nSecondly, you should authenticate pressing the Authenticate button in bot.\nAfter that, you can use our bot.")


@dp.message_handler(commands=['auth'], state=None)
async def authenticate(message: types.Message):
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
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.post('http://localhost:8000/api/v1/auth/token/login/', data=data) as resp:
            token = await resp.text()
            user = User(username=data.get('username'), password=data.get(
                'password'), token=token[15:-2], tg_user_id=message.from_user.id)
            await user.save()
            await message.answer('You successfuly authenticated!')

    await state.update_data(token=token)
    await state.finish()


@dp.message_handler(commands=['add_phrase'], state=None)
async def add_phrase(message: types.Message):
    await ExtendPhrasesGroup.source_lang.set()
    await message.answer('Select a language of source phrase, please', parse_mode='html', reply_markup=languages_keyboard())


@dp.callback_query_handler(lambda c: c.data, state=ExtendPhrasesGroup.source_lang)
async def get_first_auth_answer(query: types.CallbackQuery, state=FSMContext):
    await bot.answer_callback_query(query.id)
    answer = query.data
    await state.update_data(source_lang=answer)
    await bot.send_message(query.from_user.id, text='Select a language of target phrase, please', parse_mode='html', reply_markup=languages_keyboard())
    await ExtendPhrasesGroup.next()


@dp.callback_query_handler(lambda c: c.data, state=ExtendPhrasesGroup.target_lang)
async def get_second_auth_answer(query: types.CallbackQuery, state=FSMContext):
    answer = query.data
    await state.update_data(target_lang=answer)
    await bot.send_message(query.from_user.id, text='Now, enter the phrase to remember', parse_mode='html')
    await ExtendPhrasesGroup.next()


@dp.message_handler(state=ExtendPhrasesGroup.source_text)
async def get_third_auth_answer(message: types.Message, state=FSMContext):
    answer = message.text
    await state.update_data(source_text=answer)
    await message.answer('Enter the translation of your phrase', parse_mode='html')
    await ExtendPhrasesGroup.next()


@dp.message_handler(state=ExtendPhrasesGroup.target_text)
async def get_fourth_auth_answer(message: types.Message, state=FSMContext):
    answer = message.text
    await state.update_data(target_text=answer)
    print(await state.get_data())
    token = await User.filter(tg_user_id=message.from_user.id).first().values("token")
    data = {'Authorization': 'Token ' + token.get('token')}
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.post('http://localhost:8000/api/v1/languages/phrases', headers=data, json=await state.get_data()) as resp:
            if resp.status == 201:
                await message.answer('Phrase has been added.', reply_markup=main_keyboard())
    await state.finish()


@dp.message_handler(lambda message: message.text == "My glossary")
async def get_all_phrases(message: types.Message):
    token = await User.filter(tg_user_id=message.from_user.id).first().values("token")
    data = {'Authorization': 'Token ' + token.get('token')}
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get('http://localhost:8000/api/v1/languages/phrases', headers=data) as resp:
            for phrase in await resp.json():
                await message.answer(f"{phrase['source_text']} >>> {phrase['target_text']}")


if __name__ == "__main__":
    executor.start(dp, on_startup())
    executor.start_polling(dp, skip_updates=True)