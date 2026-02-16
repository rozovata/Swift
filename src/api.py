from fastapi.routing import APIRouter

from db import add_userr, get_user_by_user_password
from models import User
from src.db import re_userr

app = APIRouter()

#users=get_users()

# @app.get("/get_user")
# async def root1():
#     return add_user()

@app.post("/add_user")
async def add_user(user: User):
    return add_userr(user).model_dump()

@app.get("/profile")
async def profile(user: User):
    return profile(user).model_dump()

@app.post("/re_profile")
async def re_profile(user: User):
    return re_userr(user).model_dump()

@app.post("/get_profile")
async def get_profile(user: User):
    return get_user_by_user_password(user).model_dump()
