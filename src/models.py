from pydantic import BaseModel


class User(BaseModel):
    id: int = -1
    userName: str
    userPass: str
    done: bool = False

    # {"name" : "asd", "description": "asdasds"}
