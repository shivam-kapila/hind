from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    user_id: int
    category: str
    body: str
    upload_res_url: str
    tags: list
    likes: int = 0
