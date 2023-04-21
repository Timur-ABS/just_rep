from fastapi import FastAPI
from .routers import auth_router
from database import db_connection

app = FastAPI()

app.include_router(auth_router, prefix="/authentication")


@app.get("/asdf")
async def f():
    users = await db_connection.get_all_users()
    return users
