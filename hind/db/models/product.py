from datetime import date
from pydantic import BaseModel


class Product(BaseModel):
    id: int = None
    name: str
    user_id: int
    user_name: str = None
    name_of_user: str = None
    profile_picture_url: str = None
    about: str = None
    category: str
    origin_location: str
    description: str
    upload_res_url: str
    tags: list
    bids: list = []
