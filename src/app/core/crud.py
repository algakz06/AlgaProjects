from sqlalchemy import update
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from typing import Union

from app.models import db_models, models
from app.config import log


# region Users
def get_user(db: Session, tg_user_id: int) -> models.User | None:
    """
    help function for getting user from db by tg id,
    may be used to check if user exists, for editing information and etc
    """
    user = (
        db.query(db_models.Users)
        .filter(
            db_models.Users.tg_id == tg_user_id,
        )
        .first()
    )
    if not user:
        return None
    return models.User.from_orm(user)


def add_user_to_db(db: Session, tg_user_id: int):
    """adding user after command /start to db"""
    db_user = db_models.Users(tg_id=tg_user_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


# endregion
