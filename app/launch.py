from aiogram import Dispatcher, executor
from utils import IsPrivate, startup_notify


async def startup(dp: Dispatcher):
    await startup_notify(dp)
    dp.filters_factory.bind(IsPrivate)


if __name__ == "__main__":
    from chat import dp

    executor.start_polling(dp, on_startup=startup)
