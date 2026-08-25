from fastapi import APIRouter

# from src.agents.assistant import Assistant
from src.schemas.request import ChatRequest
from src.schemas.response import ChatResponse

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
async def chat_router(prompt: ChatRequest) -> ChatResponse:
    reply = await Assistant.chat(prompt.message)
    return reply

