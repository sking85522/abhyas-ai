from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shared.configs.settings import BaseAppSettings

settings = BaseAppSettings()

# Synchronous PostgreSQL URI format
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/auth_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
