# region third-party imports
from aiogram import Bot, Dispatcher, Router
import asyncio

# endregion

# region local imports
from app.config import settings
from app.handlers.start import router as start_router
from app.middlewares.db_middleware import DbSessionMiddleware
from app.core.db import init_db


# endregion
def setup_handlers(router: Router):
    """
    Setup all handlers
    """
    router.register_message_handler(start_handler, commands=["start"])


async def main():
    """Initialize bot and dispatcher"""
    bot = Bot(token=settings.TG_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    """Initialize database"""
    session = init_db()

    """Setup middlewares"""

    """Setup handlers"""
    start_router.message.middleware(DbSessionMiddleware(session))
    dp.include_router(start_router)

    """Start polling"""
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
