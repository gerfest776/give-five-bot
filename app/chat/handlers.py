from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, CommandStart
from core.loader import dp
from utils import IsPrivate


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Hello")


@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    await message.answer("Im not a support")
