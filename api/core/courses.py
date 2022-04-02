from studentvue import StudentVue
from api.utils import get_course_by_period
from .grades import get_raw_grades


# this function will just return the ordered dict
def get_raw_courses(user: StudentVue) -> list:
    return user.get_schedule()["StudentClassSchedule"]["ClassLists"]["ClassListing"]


# this function will just return the course names
def get_course_names(user: StudentVue) -> list:
    courses = get_raw_courses(user)

    return [course["@CourseTitle"] for course in courses]


def get_raw_today_courses(user: StudentVue) -> list:
    today_courses = \
        user.get_schedule()["StudentClassSchedule"]["TodayScheduleInfoData"]["SchoolInfos"]["SchoolInfo"]["Classes"][
            "ClassInfo"]
    return today_courses


# I have to write this function because when you get the @ClassName it gives some weird numbers at the end
def get_today_courses(user: StudentVue) -> list:
    all_courses = get_raw_courses(user)
    today_courses = get_raw_today_courses(user)

    today_course_names = []

    for today_course in today_courses:
        period = today_course['@Period']
        new_today_course = get_course_by_period(user, period)
        new_today_course['start_time'] = today_course['@StartTime']
        new_today_course['end_time'] = today_course['@EndTime']
        for all_course in all_courses:
            if all_course["@CourseTitle"] in new_today_course['course_name']:
                today_course_names.append(new_today_course)
    return today_course_names


def get_courses(user: StudentVue) -> list:
    grades = get_raw_grades(user)
    courses = []
    for grade in grades:
        course = get_course_by_period(user, grade['@Period'])
        marks = grade['Marks']['Mark']
        course['letter_grade'] = marks["@CalculatedScoreString"]
        course['number_grade'] = marks["@CalculatedScoreRaw"]
        courses.append(course)
    return courses
