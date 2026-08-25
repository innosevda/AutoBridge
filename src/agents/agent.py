import os

from src.agents.prompts import SYSTEM_PROMPT

from strands import Agent
from strands.models.ollama import OllamaModel
from dotenv import load_dotenv

from src.agents.calendar_tools import (
    create_calendar_event,
    list_calendar_events,
    update_calendar_event,
    delete_calendar_event,
    get_current_datetime,
)

load_dotenv()

ollama_model = OllamaModel(
    host = "https://ollama.com",
    model_id=os.getenv("OLLAMA_MODEL", "gpt-oss:120b"),
    ollama_client_args={
        "headers": {
            "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"
        },
        "verify": False
    },
    temperature=0.2,
)


agent = Agent(
    model=ollama_model,
    system_prompt=SYSTEM_PROMPT,
    tools=[
        get_current_datetime,
        create_calendar_event,
        list_calendar_events,
        update_calendar_event,
        delete_calendar_event,
    ],
)