from typing import Any

from src.auth.google_auth import get_calendar_service


CALENDAR_TIMEZONE = "Asia/Baku"


class CalendarService:

    def __init__(self):
        self.service = get_calendar_service()
        self.calendar_id = "primary"

    def create_event(
        self,
        summary: str,
        start_datetime: str,
        end_datetime: str,
        description: str = "",
        location: str = "",
    ) -> dict[str, Any]:

        event_body = {
            "summary": summary,
            "start": {
                "dateTime": start_datetime,
                "timeZone": CALENDAR_TIMEZONE,
            },
            "end": {
                "dateTime": end_datetime,
                "timeZone": CALENDAR_TIMEZONE,
            },
        }

        if description:
            event_body["description"] = description

        if location:
            event_body["location"] = location

        return (
            self.service.events()
            .insert(
                calendarId=self.calendar_id,
                body=event_body,
            )
            .execute()
        )

    def list_events(
        self,
        start_datetime: str,
        end_datetime: str,
    ) -> list[dict[str, Any]]:

        response = (
            self.service.events()
            .list(
                calendarId=self.calendar_id,
                timeMin=start_datetime,
                timeMax=end_datetime,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        return response.get("items", [])

    def get_event(
        self,
        event_id: str,
    ) -> dict[str, Any]:

        return (
            self.service.events()
            .get(
                calendarId=self.calendar_id,
                eventId=event_id,
            )
            .execute()
        )

    def update_event(
        self,
        event_id: str,
        summary: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        description: str | None = None,
        location: str | None = None,
    ) -> dict[str, Any]:

        event = self.get_event(event_id)

        if summary is not None:
            event["summary"] = summary

        if description is not None:
            event["description"] = description

        if location is not None:
            event["location"] = location

        if start_datetime is not None:
            event["start"] = {
                "dateTime": start_datetime,
                "timeZone": CALENDAR_TIMEZONE,
            }

        if end_datetime is not None:
            event["end"] = {
                "dateTime": end_datetime,
                "timeZone": CALENDAR_TIMEZONE,
            }

        return (
            self.service.events()
            .update(
                calendarId=self.calendar_id,
                eventId=event_id,
                body=event,
            )
            .execute()
        )

    def delete_event(
        self,
        event_id: str,
    ) -> None:

        self.service.events().delete(
            calendarId=self.calendar_id,
            eventId=event_id,
        ).execute()