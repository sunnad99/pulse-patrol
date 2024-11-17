from database import Base
from sqlalchemy import Column, Integer, String


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)  # TODO: Hash this and store in database

    # TODO: Add the following columns
    # fingerprint = Column(String)
