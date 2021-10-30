from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from typing import Generator

SQLACHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLACHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# inyector de dependencias
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
