from fastapi import APIRouter, Depends
from .user import get_user
from studentvue import StudentVue
from .core.events import get_events, get_upcoming_events
from typing import List
from . import schemas

router = APIRouter(prefix='/events', tags=['Events'])


@router.get('/', response_model=List[schemas.Event])
def get_all_events_route(user: StudentVue = Depends(get_user)):
    """
    Get <b>all</b> events
    """
    return get_events(user)


@router.get('/upcoming', response_model=List[schemas.Event])
def get_upcoming_events_route(user: StudentVue = Depends(get_user)):
    """
    Get all events in the <b> next seven days</b>
    """
    return get_upcoming_events(user)
