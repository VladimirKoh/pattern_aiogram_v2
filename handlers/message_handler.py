from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp, bot
from keyboards import inline, reply
from states import *


# @dp.message_handler()
# async def name(message: types.Message):


@dp.message_handler(commands=['start'])
async def command_start_process(message: types.Message):
    await message.answer("Hello, world!")