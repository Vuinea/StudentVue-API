# Student Check

## About
The backend for dashboard that uses the [StudentVue.py](https://github.com/StudentVue/StudentVue.py), along with [FastAPI](https://fastapi.tiangolo.com/)

## Contributing
1. Install packages in requirements.txt 
2. Fill up local settings with SECRET_KEY, and ALGORITHM
3. Run the code by typing `uvicorn api.main:app` in the cmd (see [here](https://fastapi.tiangolo.com/tutorial/first-steps/) for more details)
4. Get JWT from `/auth/login` by typing in studentvue credentials in form data
5. All logic is in the core folder, things for authentication are in `oauth2.py` and the pydantic models are in `schemas.py`
