import loguru
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import BoundFilter
from core.config import settings
from core.message_template import get_startup_message

logger = loguru.logger


async def startup_notify(dp: Dispatcher):
    try:
        msg: str = get_startup_message((await dp.bot.get_me()).first_name)
        await dp.bot.send_message(settings.ADMIN, msg)
    except Exception as e:
        logger.error(f"Failed startup bot: {e}")


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in [types.ChatType.PRIVATE]
