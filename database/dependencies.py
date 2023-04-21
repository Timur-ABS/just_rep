# dependencies.py
from fastapi import Depends
from .db_instance import db_connection


async def get_db():
    async with db_connection:
        yield db_connection
