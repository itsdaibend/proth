from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from utils import COUNTRY_CODES


def main_keyboard():
    buttons = [
        [KeyboardButton(text="How to use this bot?")],
        [KeyboardButton(text="Authenticate")],
        [KeyboardButton(text="My glossary")],
        [
            KeyboardButton(
                text="Save a word to the glossary",
            )
        ],
        [KeyboardButton(text="Translate random phrase")],
    ]
    keyboard = ReplyKeyboardMarkup()
    for btn in buttons:
        keyboard.add(*btn)

    return keyboard


def languages_keyboard():
    buttons = [
        [InlineKeyboardButton(text=v, callback_data=k)]
        for k, v in COUNTRY_CODES.items()
    ]
    keyboard = InlineKeyboardMarkup()
    for btn in buttons:
        keyboard.add(*btn)

    return keyboard
