from fastapi import APIRouter, Depends
from .core.assignments import get_assignments, get_weighted_assignments
from studentvue import StudentVue
from .user import get_user
from . import schemas
from typing import List

router = APIRouter(prefix='/assignments', tags=['Assignments'])


@router.get('/', response_model=List[schemas.Assignments])
def get_assignments_route(user: StudentVue = Depends(get_user), weighted: bool = False):
    """
    Get <b>all</b> assignments for the user (weighted will only give the summative grades).
    """
    a_list = get_assignments(user) if not weighted else get_weighted_assignments(user)
    return a_list


@router.get("/{course_period}", response_model=List[schemas.Assignment])
def course_assignments(course_period: int, user: StudentVue = Depends(get_user), weighted: bool = False):
    """
    Get the assignments for a certain period.
    """
    a_list = get_assignments(user) if not weighted else get_weighted_assignments(user)
    return a_list[course_period-1]['assignments']
