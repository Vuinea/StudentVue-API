from fastapi import FastAPI
from .routers import assignments, courses, grades, events, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(assignments.router)
app.include_router(grades.router)
app.include_router(events.router)


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", 'GET'],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """
    Welcome message
    """
    return {"message": "Welcome to the LCPS StudentVue API!"}
