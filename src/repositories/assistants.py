"""Table ORM definitions"""
from typing import Union, List
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import select, and_

from src.repositories.db import Base, session
from src.utils.errors import Errors
from src.utils import SystemCodes


class AssistantsTable(Base):
    """Shows table definition"""

    __tablename__ = "assistants"

    assistant_id = Column("assistant_id", Integer, primary_key=True)
    assistant_name = Column("assistant_name", String(100))
    file_path = Column("file_path", String(100))
    model = Column("model", String(100))
    created_at = Column("created_at", Date)
    created_by = Column("created_by", Date)

    @classmethod
    async def select_assistant(cls, assistantid: int):
        """Return assistant information"""
        stmt = select(
            cls.assistant_id,
            cls.assistant_name,
            cls.file_path,
            cls.model,
            cls.created_at,
            cls.created_by,
        ).where(
            cls.assistant_id == assistantid,
        )
        resp = session.execute(stmt)
        return resp
