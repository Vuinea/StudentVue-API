from fastapi.security import OAuth2PasswordBearer
from .local_settings import SECRET_KEY, ALGORITHM
from datetime import datetime, timedelta
from jose import jwt, JWTError
from . import schemas
from fastapi import status, Depends, HTTPException
from studentvue import StudentVue

ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode['exp'] = expire

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("username")
        password = payload.get('password')

        if username is None or password is None:
            raise credentials_exception

        token_data = schemas.TokenData(username=username, password=password)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    parsed_token = verify_access_token(token, credentials_exception)
    username = parsed_token.username
    password = parsed_token.password
    # not unpacking values because the keys in studentvue are private and are _username and _password
    user = StudentVue(username, password, district_domain='portal.lcps.org')
    if "RT_ERROR" in user.get_gradebook():
        user = None
    return user
