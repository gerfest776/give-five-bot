from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from chat.buttons import get_base_markup
from chat.stat import StatManager
from chat.types import ActionType
from core.loader import dp
from core.message_template import get_help_message, get_stat_message
from utils import IsPrivate


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        "Приветствую в игре 'Камень, ножницы, бумага'", reply_markup=get_base_markup()
    )


@dp.message_handler(IsPrivate(), Text(equals=[ActionType.STAT.value]))
async def bot_stat(message: types.Message):
    await message.answer(
        get_stat_message(await StatManager.repr_stat(message.from_id)),
        reply_markup=get_base_markup(),
    )


@dp.message_handler(IsPrivate(), Text(equals=[ActionType.HELP.value]))
async def bot_help(message: types.Message):
    await message.answer(get_help_message(), reply_markup=get_base_markup())


@dp.message_handler(IsPrivate(), Text(equals=[ActionType.BACK.value]))
async def bot_back(message: types.Message):
    await message.answer(text="Откатываюсь в главное меню", reply_markup=get_base_markup())
