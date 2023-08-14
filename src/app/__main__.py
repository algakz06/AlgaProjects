# region third-party imports
from aiogram import Bot, Dispatcher

import asyncio
from sqlalchemy.orm import sessionmaker

# endregion

# region local imports
from app.config import settings
from app.middlewares.db_middleware import DbSessionMiddleware
from app.middlewares.notion_middleware import NotionMiddleware
from app.core.db import init_db

# region routers
from app.handlers.start import router as start_router
from app.handlers.add_token import router as add_token_router
from app.utils.notion import Notion

# endregion


# endregion
def setup_handlers(dp: Dispatcher):
    """
    Setup all handlers
    """
    dp.include_router(start_router)
    dp.include_router(add_token_router)


def setup_middlewares(session: sessionmaker, notion: Notion):
    """
    Setup middlewares
    """
    start_router.message.middleware(DbSessionMiddleware(session))
    add_token_router.message.middleware(DbSessionMiddleware(session))
    add_token_router.message.middleware(NotionMiddleware(notion))


async def main():
    """Initialize bot and dispatcher"""
    bot = Bot(token=settings.TG_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    """Initialize database"""
    session = init_db()

    """Initialize notion"""
    notion = Notion()

    """Setup middlewares"""
    setup_middlewares(session, notion)

    """Setup handlers"""
    setup_handlers(dp)

    """Start polling"""
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
