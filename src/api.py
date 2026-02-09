from fastapi.routing import APIRouter
from db import add_user, get_tasks
from src.models import User

app = APIRouter()



@app.get("/get_tasks")
async def root():
    return get_tasks()


@app.post("/add_user")
async def add_user_request(user: User):
    return add_user(user).model_dump()




