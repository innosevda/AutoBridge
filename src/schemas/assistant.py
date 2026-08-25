from pydantic import BaseModel
from typing import Any
from enum import Enum

class Intent(str, Enum):
    CHAT = "chat"
    CREATE_EVENT = "create_calendar_event"
    UPDATE_EVENT = "update_calendar_event"
    DELETE_EVENT = "delete_calendar_event"
    LIST_EVENTS = "list_calendar_events"
    SUMMARIZE_CALENDAR = "summarize_calendar"

class AssistantResponse(BaseModel):
    intent: Intent
    parameters: dict[str, Any]
    response: str

