from pydantic import BaseModel
from typing import Optional, List, Literal


class Assignment(BaseModel):
    measure: str
    measure_description: str = ""
    earned_points: float
    total_points: float
    # major or minor summative
    assignment_type: Literal['Major', 'Minor', 'Formative']
    notes: str = ''
    # when retrieving from studentvue it gives a string, so we need to parse that in the get assignments function
    # due_date: datetime.datetime
    due_date: str


class Assignments(BaseModel):
    course_name: str
    assignments: List[Assignment]


# model for the grade route
class Grade(BaseModel):
    letter_grade: str
    number_grade: int
    course_name: str
    teacher: str
    assignments: Optional[List[Assignment]]


# model for each course on the schedule
class ScheduleCourse(BaseModel):
    period: int
    course_name: str
    room_name: str
    teacher: str
    start_time: str
    end_time: str
    meeting_days: Literal['A', "B", "A, B"]


# schema for the course route which includes all the data for the course
class FullCourse(BaseModel):
    course_name: str
    meeting_days: Literal['A', "B", "A, B"]
    letter_grade: str
    number_grade: int
    teacher: str
    period: int
    room_name: str


class Event(BaseModel):
    title: str
    date: str
    start_time: Optional[str]
    day_type: Optional[str]


# auth

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str
    password: str
