from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types.base import TelegramObject

from app.utils.notion import Notion


class NotionMiddleware(BaseMiddleware):
    def __init__(self, notion: Notion):
        super().__init__()
        self.notion = notion

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        data["notion"] = self.notion
        return await handler(event, data)
