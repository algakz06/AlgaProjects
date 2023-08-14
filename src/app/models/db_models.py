from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, nullable=False, unique=True)
    notion_token = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, default="now()")


class Databases(Base):
    __tablename__ = "databases"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    db_name = Column(String, nullable=False)
    db_id = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default="now()")
