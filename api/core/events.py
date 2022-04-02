from collections import OrderedDict

from studentvue import StudentVue
import datetime
from api.utils import get_seven_days


def get_raw_events(user: StudentVue) -> dict:
    return user.get_calendar()["CalendarListing"]["EventLists"]["EventList"]


def parse_event(event: OrderedDict) -> dict:
    event = {
        'date': event['@Date'],
        'title': event['@Title'],
        'start_time': event['@StartTime'],
        'day_type': event['@DayType']
    }
    return event


def get_events(user: StudentVue):
    events = get_raw_events(user)
    parsed_events = []
    for event in events:
        event = parse_event(event)
        parsed_events.append(event)
    return parsed_events


def get_upcoming_events(user: StudentVue):
    events = get_raw_events(user)
    seven_days = get_seven_days()
    upcoming_events = []
    for event in events:
        event_date = datetime.datetime.strptime(event['@Date'], "%m/%d/%Y").date()
        if event_date in seven_days:
            upcoming_events.append(parse_event(event))
    return upcoming_events
