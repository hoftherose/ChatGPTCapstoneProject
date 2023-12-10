"""Table ORM definitions"""
from typing import Union, List
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import select, and_

from src.repositories.db import Base, session
from src.utils.errors import Errors
from src.utils import SystemCodes


class UserTable(Base):
    """Shows table definition"""

    __tablename__ = "users"

    user_id = Column("user_id", Integer, primary_key=True)
    user_name = Column("user_name", String(100))
    user_not_so_secret = Column("user_not_so_secret", String(100))
    created_at = Column("created_at", Date)
    created_by = Column("created_by", Date)

    @classmethod
    def select_all_users(cls):
        """Return user information"""
        stmt = select(
            cls.user_id,
            cls.user_name,
            cls.user_not_so_secret,
            cls.created_at,
            cls.created_by,
        )
        resp = session.execute(stmt)
        return resp.all()

    @classmethod
    def select_user(cls, userid: int):
        """Return user information"""
        stmt = select(
            cls.user_id,
            cls.user_name,
            cls.user_not_so_secret,
            cls.created_at,
            cls.created_by,
        ).where(
            cls.user_id == userid,
        )
        resp = session.execute(stmt)
        return resp.all()