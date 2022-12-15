from aiogram.dispatcher.filters.state import StatesGroup, State


class AuthenticationGroup(StatesGroup):
    username = State()
    password = State()
    token = State()