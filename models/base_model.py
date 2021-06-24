#!/usr/bin/python3
''' Executable command '''


from uuid import uuid4
from datetime import datetime


class BaseModel:
    ''' Father class '''
    id = 0
    created_at = None
    updated_at = None

    def __init__(self):
        ''' Class constructor '''
        self.id = str(uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        ''' Str representation of the instance '''
        s = "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)
        return s

    def save(self):
        ''' Datetime last modification of object '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Dictionari representation of the instance '''
        ret_dict = self.__dict__.copy()
        ret_dict['__class__'] = BaseModel.__name__
        ret_dict['created_at'] = ret_dict['created_at'].isoformat()
        if ('updated_at' in ret_dict):
            ret_dict['updated_at'] = ret_dict['updated_at'].isoformat()
        return ret_dict
