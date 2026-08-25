from fastapi import FastAPI

from src.api.chat import router

app = FastAPI()

app.include_router(router)