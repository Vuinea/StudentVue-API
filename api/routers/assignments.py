from fastapi import APIRouter, Depends
from api.core.assignments import get_assignments, get_weighted_assignments
from studentvue import StudentVue
from api import schemas
from typing import List
from api import oauth2

router = APIRouter(prefix='/assignments', tags=['Assignments'])


@router.get('/', response_model=List[schemas.Assignments])
async def get_assignments_route(user: StudentVue = Depends(oauth2.get_current_user), weighted: bool = False):
    """
    Get <b>all</b> assignments for the user (weighted will only give the summative grades).
    """
    a_list = get_assignments(user) if not weighted else get_weighted_assignments(user)
    return a_list


@router.get("/{course_period}", response_model=List[schemas.Assignment])
async def course_assignments(course_period: int, user: StudentVue = Depends(oauth2.get_current_user), weighted: bool = False):
    """
    Get the assignments for a certain period.
    """
    a_list = get_assignments(user) if not weighted else get_weighted_assignments(user)
    return a_list[course_period-1]['assignments']
