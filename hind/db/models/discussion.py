from pydantic import BaseModel


class Discussion(BaseModel):
    id: int = None
    title: str
    user_id: int
    user_name: str = None
    name: str = None
    profile_picture_url: str = None
    category: str
    location: str = None
    body: str
    tags: list
