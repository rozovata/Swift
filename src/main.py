from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from api import app as router

app = FastAPI()
app.include_router(router, prefix="/api")
app.mount("/", StaticFiles(directory="static"), name="static")

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
