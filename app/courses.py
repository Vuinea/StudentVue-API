from fastapi import Depends, APIRouter
from studentvue import StudentVue
from .core.courses import get_courses, get_today_courses
from .user import get_user
from . import schemas
from typing import List

router = APIRouter(prefix="/courses", tags=['Courses'])


@router.get('/', response_model=List[schemas.FullCourse])
def get_courses_route(user: StudentVue = Depends(get_user)):
    """
    Get all courses
    """
    courses = get_courses(user)

    return courses


@router.get('/today', response_model=List[schemas.ScheduleCourse])
def get_today_assignments(user: StudentVue = Depends(get_user)):
    """
    Get courses for today
    """
    try:
        return get_today_courses(user)
    except KeyError as e:
        print(e)
        return {"detail": "No school today"}
