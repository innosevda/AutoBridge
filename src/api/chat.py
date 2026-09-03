from fastapi import APIRouter

from src.agents.agent import agent
from src.schemas.request import ChatRequest

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
async def chat_router(prompt: ChatRequest):
    reply = agent(prompt.message)
    return reply
