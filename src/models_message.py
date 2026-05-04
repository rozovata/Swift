from pydantic import BaseModel, Field
from datetime import datetime


class Message(BaseModel):
    id: int = -1
    user_id: int
    user_name: str = ""
    message: str
    created_at: datetime = Field(default_factory=datetime.now)

