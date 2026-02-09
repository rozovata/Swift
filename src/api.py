from fastapi.routing import APIRouter

from db import add_userr
from models import User

app = APIRouter()

#users=get_users()

# @app.get("/get_user")
# async def root1():
#     return add_user()

@app.post("/add_user")
async def add_user(user: User):
    return add_userr(user).model_dump()