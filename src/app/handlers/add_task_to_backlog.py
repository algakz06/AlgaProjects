from aiogram import types, Router
from aiogram.filters import CommandStart
from sqlalchemy.orm import Session

from app.utils.render_templates import render_template
from app.core import crud


router = Router()



