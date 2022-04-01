from fastapi import APIRouter, Depends
from .user import get_user
from studentvue import StudentVue
from .core.grades import get_grades
from app.utils import get_grades_by_period

router = APIRouter(prefix='/grades', tags=['Grades'])


@router.get('/')
def get_grades_route(user: StudentVue = Depends(get_user)):
    """
    Get <b>all</b> grades
    """
    return get_grades(user)


@router.get('/{period_num}')
def get_grade_by_period(period_num: int, user: StudentVue = Depends(get_user)):
    """
    Get grades for certain period
    """
    return get_grades_by_period(user, period_num)
