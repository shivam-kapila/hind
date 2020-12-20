import sqlalchemy
import uuid

from hind import db
from hind.db.models.user import User
from hind.db import logging


def create(user: User) -> int:
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            INSERT INTO "user" (name, user_name, email_id, password, address, about, auth_token)
                 VALUES (:name, :user_name, :email_id, crypt(:password, gen_salt('bf')), :address, :about, :auth_token)
              RETURNING id
        """), {
            "name": user.name,
            "email_id": user.email_id,
            "user_name": user.user_name,
            "password": user.password,
            "address": user.address,
            "about": user.about,
            "auth_token": str(uuid.uuid4()),
        })

        return result.fetchone()["id"]


def get(user: User):
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT id, name, user_name, email_id, address, auth_token, about, created
              FROM "user"
             WHERE user_name = :user_name
               AND password = crypt(:password, password);
        """), {
            "user_name": user.user_name,
            "password": user.password,
        })
        row = result.fetchone()
        return User(**dict(row)) if row else None


def get_by_id(id: int):
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT id, name, user_name, email_id, address, auth_token, about, created
              FROM "user"
             WHERE id = :id
        """), {"id": id})
        row = result.fetchone()
        return User(**dict(row)) if row else None


def get_by_user_name(user_name: str):
    with db.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT id, name, user_name, email_id, address, auth_token, about, created
              FROM "user"
             WHERE user_name = :user_name
        """), {"user_name": user_name})
        row = result.fetchone()
        return User(**dict(row)) if row else None
