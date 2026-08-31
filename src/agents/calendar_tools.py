from strands import tool

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from src.clients.calendar_service import CalendarService


calendar_service = CalendarService()

@tool
def create_calendar_event(
    summary: str,
    date: str,
    start_time: str,
    duration_minutes: int ,
    description: str = "",
    location: str = "",
) -> str:

    print("\n========== CREATE EVENT ==========")
    print("summary:", repr(summary))
    print("date:", repr(date))
    print("start_time:", repr(start_time))
    print("duration:", repr(duration_minutes))
    print("description:", repr(description))
    print("location:", repr(location))

    try:
        timezone = ZoneInfo("Asia/Baku")

        start = datetime.strptime(
            f"{date} {start_time}",
            "%Y-%m-%d %H:%M",
        ).replace(tzinfo=timezone)

        end = start + timedelta(minutes=duration_minutes)

        print("START:", start)
        print("START ISO:", start.isoformat())
        print("END:", end)
        print("END ISO:", end.isoformat())

        event = calendar_service.create_event(
            summary=summary,
            start_datetime=start.isoformat(),
            end_datetime=end.isoformat(),
            description=description,
            location=location,
        )

        print("GOOGLE EVENT:", event)
        print("=================================\n")

        return f"Successfully created event: {summary}"

    except Exception as e:
        print("\n========== CREATE EVENT ERROR ==========")
        print(type(e).__name__)
        print(str(e))
        print("========================================\n")

        return f"ERROR creating calendar event: {type(e).__name__}: {e}"

@tool
def list_calendar_events(
    start_datetime: str,
    end_datetime: str,
) -> str:
    """
    List calendar events within a datetime range.

    Args:
        start_datetime: Beginning of the range in ISO 8601 format.
        end_datetime: End of the range in ISO 8601 format.

    Returns:j
        Calendar events within the requested range.
    
    The user's timezone is Asia/Baku.
    """

    events = calendar_service.list_events(
        start_datetime=start_datetime,
        end_datetime=end_datetime,
    )

    if not events:
        return "No calendar events found."

    result = []

    for event in events:
        result.append(
            {
                "id": event.get("id"),
                "summary": event.get("summary"),
                "start": event.get("start"),
                "end": event.get("end"),
            }
        )

    return str(result)


@tool
def update_calendar_event(
    event_id: str,
    summary: str | None = None,
    start_datetime: str | None = None,
    end_datetime: str | None = None,
    description: str | None = None,
    location: str | None = None,
) -> str:
    """
    Update an existing Google Calendar event.

    Args:
        event_id: Google Calendar event ID.
        summary: New title, if changing it.
        start_datetime: New start datetime, if changing it.
        end_datetime: New end datetime, if changing it.
        description: New description, if changing it.
        location: New location, if changing it.
    
    The user's timezone is Asia/Baku.
    """

    event = calendar_service.update_event(
        event_id=event_id,
        summary=summary,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        description=description,
        location=location,
    )

    return f"Event '{event.get('summary')}' updated successfully."

@tool
def delete_calendar_event(event_id: str) -> str:
    """
    Delete a Google Calendar event.

    Args:
        event_id: ID of the event to delete.

    The user's timezone is Asia/Baku.
    """

    calendar_service.delete_event(event_id)

    return f"Event {event_id} deleted successfully."

# @tool
# def get_current_datetime() -> str:
#     """
#     Get the current date and time in the user's timezone.

#     The user's timezone is Asia/Baku.
#     """

#     now = datetime.now(
#         ZoneInfo("Asia/Baku")
#     )

#     return now.isoformat()

@tool
def get_current_datetime() -> str:
    """Return the current date and time in Asia/Baku."""

    now = datetime.now(ZoneInfo("Asia/Baku"))

    result = now.strftime("%Y-%m-%d %H:%M:%S %Z")

    print("CURRENT DATETIME TOOL RESULT:", result)

    return result