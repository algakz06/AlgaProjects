# region third-party imports
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import asyncio

# endregion

# region local imports
from app.config import settings
from app.handlers.start import start as start_handler
from app.core.db import init_db


# endregion
def setup_handlers(dp: Dispatcher):
    """
    Setup all handlers
    """
    dp.register_message_handler(start_handler, commands=["start"])


async def main():
    """Initialize bot and dispatcher"""
    bot = Bot(token=settings.TG_TOKEN, parse_mode="HTML")
    dp = Dispatcher(bot)

    """Initialize database"""
    init_db()

    """Setup handlers"""
    setup_handlers(dp)

    """Start polling"""
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
