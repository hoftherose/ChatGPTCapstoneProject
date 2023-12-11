"""Table ORM definitions"""
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import select, insert

from src.repositories.db import Base, session


class AssistantsTable(Base):
    """Shows table definition"""

    __tablename__ = "assistants"

    id = Column("id", Integer, primary_key=True)
    assistant_id = Column("assistant_id", String(100))
    assistant_name = Column("assistant_name", String(100))
    thread_id = Column("thread_id", String(100))
    file_path = Column("file_path", String(100))
    model = Column("model", String(100))
    created_at = Column("created_at", Date)

    @classmethod
    def select_assistant(cls, assistant_id: int):
        """Return assistant information"""
        stmt = select(
            cls.id,
            cls.assistant_id,
            cls.assistant_name,
            cls.thread_id,
            cls.file_path,
            cls.model,
            cls.created_at,
        ).where(
            cls.assistant_id == assistant_id,
        )
        resp = session.execute(stmt)
        return resp

    @classmethod
    def insert_assistant(cls, assistant_id, name, thread_id, path, model: str):
        """Insert assistant information"""
        stmt = insert(cls).values(
            assistant_id=assistant_id,
            assistant_name=name,
            thread_id=thread_id,
            file_path=path,
            model=model,
        )
        session.execute(stmt)
