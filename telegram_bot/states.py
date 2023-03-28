from aiogram.dispatcher.filters.state import State, StatesGroup


class AuthenticationGroup(StatesGroup):
    username = State()
    password = State()
    token = State()


class ExtendPhrasesGroup(StatesGroup):
    source_lang = State()
    target_lang = State()
    source_text = State()
    target_text = State()
