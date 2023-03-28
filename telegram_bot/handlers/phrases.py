import aiohttp
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards import languages_keyboard, main_keyboard
from misc import *
from models import User
from states import ExtendPhrasesGroup


@dp.message_handler(text="Save a word to the glossary", state=None)
async def add_phrase_callback(message: types.Message):
    await message.answer(
        text="Select a language of source phrase, please",
        parse_mode="html",
        reply_markup=languages_keyboard(),
    )
    await ExtendPhrasesGroup.source_lang.set()


@dp.callback_query_handler(lambda c: c.data, state=ExtendPhrasesGroup.source_lang)
async def get_first_auth_answer(query: types.CallbackQuery, state=FSMContext):
    await bot.answer_callback_query(query.id)
    answer = query.data
    await state.update_data(source_lang=answer)
    await bot.send_message(
        query.from_user.id,
        text="Select a language of target phrase, please",
        parse_mode="html",
        reply_markup=languages_keyboard(),
    )
    await ExtendPhrasesGroup.next()


@dp.callback_query_handler(lambda c: c.data, state=ExtendPhrasesGroup.target_lang)
async def get_second_auth_answer(query: types.CallbackQuery, state=FSMContext):
    answer = query.data
    await state.update_data(target_lang=answer)
    await bot.send_message(
        query.from_user.id, text="Now, enter the phrase to remember", parse_mode="html"
    )
    await ExtendPhrasesGroup.next()


@dp.message_handler(state=ExtendPhrasesGroup.source_text)
async def get_third_auth_answer(message: types.Message, state=FSMContext):
    answer = message.text
    await state.update_data(source_text=answer)
    await message.answer("Enter the translation of your phrase", parse_mode="html")
    await ExtendPhrasesGroup.next()


@dp.message_handler(state=ExtendPhrasesGroup.target_text)
async def get_fourth_auth_answer(message: types.Message, state=FSMContext):
    answer = message.text
    await state.update_data(target_text=answer)
    token = await User.filter(tg_user_id=message.from_user.id).first().values("token")
    data = {"Authorization": "Token " + token.get("token")}
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.post(
            "http://localhost:8000/api/v1/languages/phrases",
            headers=data,
            json=await state.get_data(),
        ) as resp:
            if resp.status == 201:
                await message.answer(
                    "Phrase has been added.", reply_markup=main_keyboard()
                )
    await state.finish()


@dp.message_handler(lambda message: message.text == "My glossary")
async def get_all_phrases(message: types.Message):
    token = await User.filter(tg_user_id=message.from_user.id).first().values("token")
    data = {"Authorization": "Token " + token.get("token")}
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(
            "http://localhost:8000/api/v1/languages/phrases", headers=data
        ) as resp:
            for phrase in await resp.json():
                await message.answer(
                    f"{phrase['source_text']} >>> {phrase['target_text']}",
                    reply_markup=main_keyboard(),
                )
