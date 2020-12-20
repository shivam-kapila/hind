from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int = None
    name: str = None
    user_name: str
    email_id: str = None
    about: str = None
    password: str = None
    address: str = None
    created: datetime = None
    auth_token: str = None
