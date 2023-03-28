from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


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
    ]
    keyboard = ReplyKeyboardMarkup()
    for btn in buttons:
        keyboard.add(*btn)

    return keyboard


def languages_keyboard():
    buttons = [
        [InlineKeyboardButton(text="English", callback_data="EN")],
        [InlineKeyboardButton(text="Ukrainian", callback_data="UA")],
        [InlineKeyboardButton(text="Russian", callback_data="RU")],
        [InlineKeyboardButton(text="German", callback_data="DE")],
        [InlineKeyboardButton(text="Polish", callback_data="PL")],
        [InlineKeyboardButton(text="Italian", callback_data="IT")],
        [InlineKeyboardButton(text="French", callback_data="FR")],
        [InlineKeyboardButton(text="Spanish", callback_data="ES")],
        [InlineKeyboardButton(text="Turkish", callback_data="TR")],
    ]
    keyboard = InlineKeyboardMarkup()
    for btn in buttons:
        keyboard.add(*btn)

    return keyboard
