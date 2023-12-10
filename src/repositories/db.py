"""Database connection used for SQLAlchemy ORM"""
import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

ADDRESS = os.getenv("DB_ADDRESS")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASS")
DATABASE = os.getenv("DB_NAME")

engine = create_async_engine(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{ADDRESS}/{DATABASE}",
    pool_size=20,
    isolation_level="AUTOCOMMIT",
)
Session = sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)
session = Session()
Base = declarative_base()
