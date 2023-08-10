from aiogram import types
from sqlalchemy.orm import Session

from app.utils.render_templates import render_template
from app.core.dependencies import get_db
from app.core import crud


async def start(message: types.Message):
    db: Session = get_db()
    user = crud.get_user(db, message.from_user.id)
    if user:
        await message.answer("Вы уже зарегистрированы")
        return

    answer = render_template("start.j2")
    await message.answer(answer)
    crud.add_user_to_db(db, message.from_user.id)
