from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from api import schemas, oauth2, utils
from studentvue import StudentVue

router = APIRouter(prefix='/auth', tags=['Authentication'])


@router.post('/login', response_model=schemas.Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    """
    Type in StudentVue credentials in order to get token
    """
    user = StudentVue(user_credentials.username, user_credentials.password, 'portal.lcps.org')
    username = user._username
    password = user._password
    if not utils.verify(user):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    access_token = oauth2.create_access_token(data={"username": username, "password": password})

    # create token
    return {"access_token": access_token, 'token_type': 'bearer'}
