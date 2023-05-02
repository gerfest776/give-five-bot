from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, CommandStart
from chat.buttons import base_markup
from chat.types import ActionType
from core.loader import dp
from utils import IsPrivate


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Hello")


@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    await message.answer("Im not a support", reply_markup=base_markup)


@dp.message_handler(IsPrivate(), commands=[ActionType.GAME.value])
async def bot_game(message: types.Message):
    await message.answer("Game starting", reply_markup=base_markup)


@dp.message_handler(IsPrivate(), commands=[ActionType.STAT.value])
async def bot_stat(message: types.Message):
    await message.answer("Your statistic", reply_markup=base_markup)
