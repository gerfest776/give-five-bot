from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from chat.buttons import get_finish_game_markup, get_game_markup
from chat.stat import StatManager
from chat.types import ActionType, CuEFaResult, CuEFaType
from core.loader import dp
from core.message_template import get_finish_game_message, get_game_message
from utils import IsPrivate


@dp.message_handler(IsPrivate(), Text(equals=[ActionType.GAME.value]))
async def bot_game(message: types.Message):
    await message.answer(get_game_message(), reply_markup=get_game_markup())


@dp.message_handler(IsPrivate(), lambda message: message.text in CuEFaType.get_values())
async def bot_check_result(message: types.Message):
    player_result: CuEFaType = CuEFaType(message.md_text)
    bot_result: CuEFaType = CuEFaType.get_random_enum()
    result: CuEFaResult = player_result == bot_result
    await StatManager.save_user_file(message.from_id, result)
    await message.answer(
        get_finish_game_message(opponent_choice=bot_result.value, result=result.value),
        reply_markup=get_finish_game_markup(),
    )
