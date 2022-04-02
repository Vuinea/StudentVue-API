from fastapi import APIRouter, Depends
from studentvue import StudentVue
from api.core.grades import get_grades
from api.utils import get_grades_by_period
from api import oauth2

router = APIRouter(prefix='/grades', tags=['Grades'])


@router.get('/')
def get_grades_route(user: StudentVue = Depends(oauth2.get_current_user)):
    """
    Get <b>all</b> grades
    """
    return get_grades(user)


@router.get('/{period_num}')
def get_grade_by_period(period_num: int, user: StudentVue = Depends(oauth2.get_current_user)):
    """
    Get grades for certain period
    """
    return get_grades_by_period(user, period_num)
