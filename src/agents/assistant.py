# Main assistant logic

from src.clients.ollama_client import chat 

class Assistant:
    async def chat(message: str):
        return await chat(message)       

