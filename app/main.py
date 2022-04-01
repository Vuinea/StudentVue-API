from fastapi import FastAPI
from . import assignments, courses, grades, events

app = FastAPI()

app.include_router(courses.router)
app.include_router(assignments.router)
app.include_router(grades.router)
app.include_router(events.router)


@app.get("/")
async def root():
    """
    Welcome message
    """
    return {"message": "Welcome to the LCPS StudentVue API!"}
