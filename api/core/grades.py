from studentvue import StudentVue
from api.utils import get_course_by_period


def get_raw_grades(user: StudentVue):
    grades = user.get_gradebook()["Gradebook"]["Courses"]["Course"]
    return grades


def get_grades(user: StudentVue):
    grades = get_raw_grades(user)
    courses = []
    for grade in grades:
        full_course = get_course_by_period(user, grade['@Period'])
        course = {}
        marks = grade['Marks']['Mark']
        course['course_name'] = full_course['course_name']
        course['letter_grade'] = marks["@CalculatedScoreString"]
        course['number_grade'] = marks["@CalculatedScoreRaw"]
        courses.append(course)
    return courses
