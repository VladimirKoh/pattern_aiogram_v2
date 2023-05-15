from aiogram.dispatcher.filters.state import State, StatesGroup


class UserStateGroup(StatesGroup):
    state_start = State()