from datetime import datetime
from pydantic import BaseModel
from flask_login import UserMixin


class User(BaseModel, UserMixin):
    id: int = None
    name: str = None
    user_name: str
    email_id: str = None
    about: str = None
    password: str = None
    address: str = None
    created: datetime = None
    auth_token: str = None
