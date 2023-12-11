"""Table ORM definitions"""
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import select, insert

from src.repositories.db import Base, session


class QuestionsTable(Base):
    """Shows table definition"""

    __tablename__ = "questions"

    id = Column("id", Integer, primary_key=True)
    thread_id = Column("thread_id", String(100))
    question = Column("question", String(240))
    created_at = Column("created_at", Date)

    @classmethod
    def list_question(cls, thread_id: str):
        """Return question information"""
        stmt = select(
            cls.id,
            cls.thread_id,
            cls.question,
            cls.created_at,
        ).where(
            cls.thread_id == thread_id,
        )
        resp = session.execute(stmt)
        return resp

    @classmethod
    def select_question(cls, id: int):
        """Return question information"""
        stmt = select(
            cls.id,
            cls.thread_id,
            cls.question,
            cls.created_at,
        ).where(
            cls.id == id,
        )
        resp = session.execute(stmt)
        return resp

    @classmethod
    def insert_question(cls, thread_id, question: str):
        """Insert question information"""
        stmt = insert(cls).values(
            thread_id=thread_id,
            question=question,
        )
        session.execute(stmt)
