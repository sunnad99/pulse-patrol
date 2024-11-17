from config import (
    POSTGRES_DB,
    POSTGRES_HOST,
    POSTGRES_USER_ENCODED,
    POSTGRES_PORT,
    POSTGRES_PASSWORD_ENCODED,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Construct the database URL
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER_ENCODED}:{POSTGRES_PASSWORD_ENCODED}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
