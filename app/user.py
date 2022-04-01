from studentvue import StudentVue
from .local_settings import USERNAME, PASSWORD

def get_user():
    user = StudentVue(USERNAME, PASSWORD, 'portal.lcps.org')
    return user

