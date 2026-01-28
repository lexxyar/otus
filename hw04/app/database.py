import urllib.parse

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_DRIVER = os.getenv('DB_PORT')

connection_string = urllib.parse.urlunparse((
    DB_DRIVER,
    f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}",
    DB_NAME,
    "",
    "",
    "",
))

print(connection_string, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME)

engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
