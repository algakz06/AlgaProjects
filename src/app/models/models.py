from pydantic import BaseModel, ConfigDict
from typing import Optional


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    tg_id: int
    notion_token: Optional[str] = None
