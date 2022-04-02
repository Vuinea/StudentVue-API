from fastapi import APIRouter, Depends
from studentvue import StudentVue
from api.core.events import get_events, get_upcoming_events
from typing import List
from api import schemas
from api import oauth2

# TODO: import oauth2

router = APIRouter(prefix='/events', tags=['Events'])


@router.get('/', response_model=List[schemas.Event])
def get_all_events_route(user: StudentVue = Depends(oauth2.get_current_user)):
    """
    Get <b>all</b> events
    """
    return get_events(user)


@router.get('/upcoming', response_model=List[schemas.Event])
def get_upcoming_events_route(user: StudentVue = Depends(oauth2.get_current_user)):
    """
    Get all events in the <b> next seven days</b>
    """
    return get_upcoming_events(user)
