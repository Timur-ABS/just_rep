# auth_routers.py
from fastapi import APIRouter
from database import db_connection
from pydantic import BaseModel
import re
import bcrypt


def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))


auth_router = APIRouter()


class Registration(BaseModel):
    email: str
    login: str
    password: str
    referral_name: str


@auth_router.post("/registration")
async def registration(new_user: Registration):

    if not is_valid_email(new_user.email):
        return {"error": False, "message": "email is invalid"}
    query_all_email = "SELECT * FROM users WHERE email = %s"
    await db_connection.execute(query_all_email, (new_user.email,))
    if await db_connection.fetchone() is None:
        query_all_login = "SELECT * FROM users WHERE login = %s"
        await db_connection.execute(query_all_login, (new_user.login,))
        if await db_connection.fetchone() is None:
            referral = None
            query_check_referral = "SELECT * FROM users where login = %s"
            await db_connection.execute(query_check_referral, (new_user.referral_name,))
            referral = await db_connection.fetchone()
            if referral is None:
                query_check_referral = "SELECT * FROM users where email = %s"
                await db_connection.execute(query_check_referral, (new_user.referral_name,))
            if referral is None:
                query_add_user = """
                    INSERT INTO users (email, login, password) VALUES (%s, %s, %s)
                """
                await db_connection.execute(query_add_user,
                                            (new_user.email, new_user.login,
                                             bcrypt.hashpw(new_user.password.encode("utf-8"), bcrypt.gensalt()),
                                             ))
            else:
                query_add_user = """
                                    INSERT INTO users (email, login, password, referral_name, referral_id) VALUES (%s, %s, %s, %s, %s)
                                """
                await db_connection.execute(query_add_user,
                                            (new_user.email, new_user.login,
                                             bcrypt.hashpw(new_user.password.encode("utf-8"), bcrypt.gensalt()),
                                             referral[2],
                                             referral[0]
                                             ))
            await db_connection.commit()
            if await db_connection.affected_rows() == 1:
                return {"error": False}
            return {"error": True}
        else:
            return {"error": True, "message": "recurring login"}
    else:
        return {"error": True, "message": "recurring mail"}

# curl -X POST "http://127.0.0.1:8000/authentication/registration" -H "accept: application/json" -H "Content-Type: application/json" -d '{"id": 1, "email": "user@example.com", "login": "user1", "password": "password", "new_password": "new_password", "referral_id": 0, "referral_name": "referral", "balance": 100, "sbros_time": 0, "email_ras": 1, "amount_bet": 0, "free_bet": 0, "role": "user"}'
