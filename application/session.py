from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application.models import dao

from application.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
dao.Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)