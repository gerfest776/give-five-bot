from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from chat.handler import startup_notify
from core.config import settings

dp: Dispatcher = Dispatcher(
    Bot(
        token=settings.API_TOKEN,
        parse_mode=types.ParseMode.MARKDOWN
    ),
    storage=MemoryStorage()
)

if __name__ == '__main__':
    executor.start_polling(
        dp,
        on_startup=startup_notify
    )
