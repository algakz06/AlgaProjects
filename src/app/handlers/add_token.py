from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from sqlalchemy.orm import Session

from app.utils.render_templates import render_template
from app.core import crud
from app.utils.notion import Notion


class AddToken(StatesGroup):
    token = State()


router = Router()


@router.message(Command("add_token"))
async def ask_adding_token(
    message: types.Message,
    session: Session,
    state: FSMContext,
):
    user = crud.get_user(session, message.from_user.id)
    if not user:
        await message.answer("Вы не зарегистрированы, напишите /start")
        return

    if user.notion_token:
        await message.answer(
            "У вас уже есть токен, чтобы его изменить, напишите /update_token"
        )
        return

    await message.answer("Введите токен, который вы получили в Notion")

    await state.set_state(AddToken.token)


@router.message(AddToken.token)
async def add_token(
    message: types.Message,
    session: Session,
    notion: Notion,
    state: FSMContext,
):
    token = message.text

    if not notion.check_token(token):
        await message.answer("Токен не валидный, попробуйте еще раз")
        return

    crud.add_notion_token(session, message.from_user.id, token)

    await message.answer("Токен успешно добавлен")

    await state.clear()
