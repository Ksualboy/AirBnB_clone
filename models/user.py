#!/usr/bin/python3
''' Executable command '''


from models.base_model import BaseModel


class User(BaseModel):
    ''' General User class '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
