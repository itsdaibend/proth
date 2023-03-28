import database
from aiogram import types
from aiogram.utils import executor
from handlers.authentication import *
from handlers.phrases import *
from keyboards import main_keyboard
from misc import *


async def on_startup():
    await database.setup()


@dp.message_handler(commands=["start"])
async def start_chat(message: types.Message):
    await message.answer(
        f"<b>Welcome, {message.from_user.first_name}!</b>",
        parse_mode="html",
        reply_markup=main_keyboard(),
    )


@dp.message_handler(lambda message: message.text == "How to use this bot?")
async def how_to_use_this_bot(message: types.Message):
    await message.reply(
        "For now, you can learn new words in different languages and translate them.\n\nFirstly, you have to visit our site and register there.\nSecondly, you should authenticate by pressing the Authenticate button in the bot.\nAfter that, you can use our bot.",
        reply_markup=main_keyboard(),
    )


if __name__ == "__main__":
    executor.start(dp, on_startup())
    executor.start_polling(dp, skip_updates=True)
