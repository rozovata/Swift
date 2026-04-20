import os

from fastapi.routing import APIRouter
from starlette.staticfiles import StaticFiles

from src.db import add_userr, get_user_by_user_password, add_message_db
from src.models import User
from src.db import re_userr
from src.models_message import Message

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
# message
@app.post("/add_message")
async def add_message(message: Message):
    return add_message_db(message).model_dump()