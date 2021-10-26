from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLACHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLACHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
