import httpx 

from src.config import OLLAMA_MODEL, OLLAMA_BASE_URL

async def chat(prompt: str, model: str = OLLAMA_MODEL):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            OLLAMA_BASE_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=60.0
        )

    response.raise_for_status() 
    
    data = response.json()
    return data["response"]