import logging

import aiohttp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import main_keyboard
from misc import *
from models import User
from states import AuthenticationGroup


@dp.message_handler(lambda message: message.text == "Authenticate", state=None)
async def authenticate(message: types.Message):
    logging.info(
        'Handler "Authenticate" has been called by User {message.from_user.id}.'
    )
    await message.answer(
        "Enter your username on Proth website:",
        parse_mode="html",
        reply_markup=main_keyboard(),
    )
    await AuthenticationGroup.username.set()


@dp.message_handler(state=AuthenticationGroup.username)
async def get_first_auth_answer(message: types.Message, state: FSMContext):
    logging.info(
        f'Handler "Authenticate" has been called by User {message.from_user.id}, state Username = {message.text}'
    )
    answer = message.text
    await state.update_data(username=answer)
    await message.answer("Enter your password on Proth website:")
    await AuthenticationGroup.next()


@dp.message_handler(state=AuthenticationGroup.password)
async def get_second_auth_answer(message: types.Message, state: FSMContext):
    logging.info(
        f'Handler "Authenticate" has been called by User {message.from_user.id}, state Password.'
    )
    answer = message.text
    await state.update_data(password=answer)

    data = await state.get_data()
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.post(
            "http://localhost:8000/api/v1/auth/token/login/", data=data
        ) as resp:
            if resp.status == 200:
                logging.info(
                    f"Successful authentication for User {message.from_user.id}."
                )
                token = await resp.text()
                user = User(
                    username=data.get("username"),
                    password=data.get("password"),
                    token=token[15:-2],
                    tg_user_id=message.from_user.id,
                )
                await user.save()
                await message.answer("You successfuly authenticated!")
                await state.update_data(token=token)
            else:
                logging.info(
                    f"Unsuccessful authentication for User {message.from_user.id}."
                )
                await message.answer("This user does not exist.")
    await state.finish()
