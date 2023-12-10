"""Table ORM definitions"""
from typing import Union, List
from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy import select, and_

from src.repositories.db import Base, session
from src.utils.errors import Errors
from src.utils import SystemCodes


class ThreadTable(Base):
    """Shows table definition"""

    __tablename__ = "threads"

    thread_id = Column("thread_id", Integer, primary_key=True)
    thread_name = Column("thread_name", String(100))
    user_id = Column("user_id", Integer, ForeignKey("user_view.user_id"))
    assistant_id = Column("assistant_id", Integer, ForeignKey("assistant_view.assistant_id"))
    created_at = Column("created_at", Date)
    created_by = Column("created_by", Date)

    @classmethod
    def select_thread(cls, threadid: int):
        """Return thread information"""
        stmt = select(
            cls.thread_id,
            cls.thread_name,
            cls.user_id,
            cls.assistant_id,
            cls.created_at,
            cls.created_by,
        ).where(
            cls.thread_id == threadid,
        )
        resp = session.execute(stmt)
        return resp
