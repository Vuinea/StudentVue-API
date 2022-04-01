import datetime

from studentvue import StudentVue
from .courses import get_course_names


def format_assignment_name(assignment_name: str) -> str:
    assignment_name = assignment_name.strip()
    number_start = assignment_name.find("(")

    return assignment_name[0:number_start]


def get_points(points: str) -> dict:
    # if the assignment has not been graded yet
    if "Points Possible" in points:
        earned_points = -1
        total_points = float(points.replace("Points Possible", ""))
    else:
        points = points.strip().split('/')
        earned_points = float(points[0].replace('Points Possible', ''))
        total_points = float(points[1])
    return {"earned_points": earned_points, "total_points": total_points}


def format_assignment_type(type_str: str):
    type_str = type_str.capitalize()
    if type_str == "Formal formative":
        type_str = "Formative"
    elif type_str == "Minor summative":
        type_str = 'Minor'
    elif type_str == "Major summative":
        type_str = 'Major'
    return type_str


def get_courses_with_assignments(user: StudentVue) -> list:
    courses = user.get_gradebook()["Gradebook"]["Courses"]["Course"]
    courses_with_assignments = []
    for course in courses:
        assignments = []

        title = format_assignment_name(course['@Title']).strip()
        raw_assignments = course["Marks"]['Mark']['Assignments']["Assignment"]
        if not isinstance(raw_assignments, list):
            raw_assignments = [raw_assignments]
        for assignment in raw_assignments:
            due_date = assignment['@DueDate']
            points = get_points(assignment['@Points'])
            assignment_type = format_assignment_type(assignment['@Type'])
            # filtering out just the fields I need
            assignment = {
                "measure": assignment["@Measure"],
                "measure_description": assignment["@MeasureDescription"],
                "total_points": points['total_points'],
                "earned_points": points['earned_points'],
                "assignment_type": assignment_type,
                "due_date": due_date,
                "notes": assignment['@Notes']
            }
            assignments.append(assignment)
        title_and_assignments = {"course_name": title, "assignments": assignments}

        courses_with_assignments.append(title_and_assignments)
    return courses_with_assignments


def get_assignments(user: StudentVue):
    assignment_courses = get_courses_with_assignments(user)
    courses = get_course_names(user)
    # if there is an assignment that does not have any grades then it will not show up in the function above so I
    # inserted it here
    for index, a_course in enumerate(assignment_courses):
        course_name = courses[index]
        if course_name != a_course['course_name']:
            assignment_courses.insert(index,
                                      {"course_name": course_name, "assignments": []})
    return assignment_courses


def get_weighted_assignments(user: StudentVue) -> list:
    courses = get_assignments(user)
    weighted_assignments = []

    for course in courses:
        # grabbing 1st element because the 0th element is the course name and the second element is the assignments
        course = course[1]
        course_assignments = []
        for a in course:
            if "formative" not in a["type"].lower() and 'not for grading' not in a['type'].lower():
                course_assignments.append(a)

        weighted_assignments.append(course_assignments)

    return weighted_assignments
