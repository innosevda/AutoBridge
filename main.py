from fastapi import FastAPI

from src.routers.chat import router

app = FastAPI()

app.include_router(router)