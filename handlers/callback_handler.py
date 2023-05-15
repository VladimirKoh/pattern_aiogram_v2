from aiogram.dispatcher.filters import Text
from aiogram import types
from loader import dp, bot
from keyboards import inline, reply
from states import *


# @dp.callback_query_handler(Text())
# async def name(callback: types.Callback):


@dp.callback_query_handler(Text(equals='test'))
async def ccallback_test(callback: types.CallbackQuery):
    pass