from fastapi import APIRouter

from src.agents.assistant import Assistant
from src.schemas.request import ChatRequest

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
async def chat_router(prompt: ChatRequest):
    reply = await Assistant.chat(prompt.message)
    return {"reply": reply}

