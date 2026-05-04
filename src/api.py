import os

from fastapi import FastAPI
from fastapi.routing import APIRouter
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
import socketio
from src.db import add_userr, get_user_by_user_password, add_message_db
from src.models import User
from src.db import re_userr
from src.models_message import Message
from src.db import get_all_messages

# Создаём обычное FastAPI-приложение.
fastapi_app = FastAPI()
router = APIRouter()

# Создаём Socket.IO сервер.
# async_mode="asgi" нужен для работы с FastAPI / Uvicorn.
sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*"
)


# @app.get("/get_user")
# async def root1():
#     return add_user()

@router.post("/add_user")
async def add_user(user: User):
    return add_userr(user).model_dump()

@router.get("/profile")
async def profile(user: User):
    return profile(user).model_dump()

@router.post("/re_profile")
async def re_profile(user: User):
    return re_userr(user).model_dump()

@router.post("/get_profile")
async def get_profile(user: User):
    return get_user_by_user_password(user).model_dump()



@router.get("/get_messages")
async def get_messages():
    return get_all_messages()

# Главная страница.
# При открытии http://localhost:3000 отдаём HTML-файл.
@router.get("/")
async def index():
    return FileResponse("public/index.html")

# Событие подключения пользователя к сокету.
@sio.event
async def connect(sid, environ):
    print("user connected:", sid)

# Событие отключения пользователя.
@sio.event
async def disconnect(sid):
    print("user disconnected:", sid)

# Событие получения сообщения от клиента.
@sio.on("chat message")
async def chat_message(sid, msg):
    print("message:", msg)
    saved_msg = add_message_db(Message(**msg))

    # Превращаем дату в строку (это единственное что нужно добавить!)
    data = saved_msg.model_dump()
    data["created_at"] = str(data["created_at"])  # или data["created_at"].isoformat()

    await sio.emit("chat message", data)

fastapi_app.include_router(router, prefix="/api")
fastapi_app.mount("/", StaticFiles(directory="static"), name="static")

app = socketio.ASGIApp(
    socketio_server=sio,
    other_asgi_app=fastapi_app
)