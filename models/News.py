import datetime
from pydantic import BaseModel
class News(BaseModel):
    id: int
    title: str
    summary: str
    content: str
    author: str
    published: bool = False
    published_at: datetime
