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
    profile_picture_url: str = 'https://www.kindpng.com/picc/m/22-223965_no-profile-picture-icon-circle-member-icon-png.png'
    created: datetime = None
    auth_token: str = None
