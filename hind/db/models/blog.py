from pydantic import BaseModel


class Blog(BaseModel):
    id: int = None
    title: str
    user_id: int
    user_name: str = None
    name: str = None
    profile_picture_url: str = None
    about: str = None
    category: str
    location: str
    body: str
    upload_res_url: str
    tags: list
    likes: int = 0
