#!/usr/bin/env python3

"""
Create 'bank' database
"""

import os

from dotenv import load_dotenv

from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base


load_dotenv(override=True)


USER = os.getenv("USER", "No such user.")
PASSWORD = os.getenv("PASSWORD", "Incorrect password.")
HOST = os.getenv("HOST", "Error when connecting.")
DB = os.getenv("DB", "Database not found.")

Base = declarative_base()


def create_database():
    try:
        engine = create_engine(f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}/")
    except MySQLdb.Error as error:
        print(f"Error: {error}")
        return

    with engine.connect() as connected:
        connected.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB}"))
        connected.commit()
    return engine


def get_engine():
    return create_engine(f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}/{DB}")


if __name__ == "__main__":
    create_database()
