import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

DB_ENGINE = os.environ.get("DB_ENGINE", "postgresql")
DB_USER = os.environ.get("DB_USER", "fastapi_user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "fastapi_password")
DB_URL = os.environ.get("DB_URL", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "fastapi_db")


CONNECTION_STRING = (
    f"{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_URL}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(CONNECTION_STRING)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
