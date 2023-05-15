from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard_test() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('test', callback_data='test')
    ikb.add(ib1)
    return ikb