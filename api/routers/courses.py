from fastapi import Depends, APIRouter
from studentvue import StudentVue
from api.core.courses import get_courses, get_today_courses
from api import schemas
from typing import List
from api import oauth2

router = APIRouter(prefix="/courses", tags=['Courses'])


@router.get('/', response_model=List[schemas.FullCourse])
async def get_courses_route(user: StudentVue = Depends(oauth2.get_current_user)):
    """
    Get all courses
    """
    courses = get_courses(user)

    return courses


@router.get('/today', response_model=List[schemas.ScheduleCourse])
async def get_today_assignments(user: StudentVue = Depends(oauth2.get_current_user)):
    """
    Get courses for today
    """
    try:
        return get_today_courses(user)
    except KeyError:
        return {"detail": "No school today"}
