from fastapi import FastAPI
from .routers import assignments, courses, grades, events, auth

app = FastAPI()

app.include_router(auth.router)
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
