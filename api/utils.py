import datetime

from studentvue import StudentVue


def get_course_by_period(user: StudentVue, period_num: int):
    courses = user.get_schedule()["StudentClassSchedule"]["ClassLists"]["ClassListing"]
    for course in courses:
        if course['@Period'] == period_num:
            course = {
                'period': course['@Period'],
                'course_name': course['@CourseTitle'],
                "room_name": str(course['@RoomName']),
                "teacher": course['@Teacher'],
                "meeting_days": course['@MeetingDays'],
            }
            return course


def get_grades_by_period(user: StudentVue, period_num: int):
    grades = user.get_gradebook()["Gradebook"]["Courses"]["Course"]
    grades_dict = {}
    for grade in grades:
        if grade['@Period'] == period_num:
            marks = grade['Marks']['Mark']
            grades_dict['letter_grade'] = marks["@CalculatedScoreString"]
            grades_dict['number_grade'] = marks["@CalculatedScoreRaw"]
            break
    return grades_dict


# for events

def get_seven_days() -> list:
    seven_days = []
    today = datetime.date.today()
    for day_num in range(0, 7):
        day = today + datetime.timedelta(days=day_num)
        seven_days.append(day)
    return seven_days


def verify(user: StudentVue):
    error = "RT_ERROR" in user.get_gradebook().keys()
    return not error
