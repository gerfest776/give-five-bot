from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from core.config import settings

dp: Dispatcher = Dispatcher(
    Bot(token=settings.BOT_TOKEN, parse_mode=types.ParseMode.HTML), storage=MemoryStorage()
)
