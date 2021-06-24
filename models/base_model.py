#!/usr/bin/python3
''' Executable command '''


from uuid import uuid4
from datetime import datetime


class BaseModel:
    ''' Father class '''
    id = 0
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        ''' Class constructor '''
        if (len(kwargs) == 0):
            self.id = str(uuid4())
            self.created_at = datetime.now()
            return

        for key in kwargs:
            if key == "__class__":
                continue
            print("{} - {}".format(key, kwargs[key]))
            if key == "created_at" or key == "updated_at":
                self.__dict__[key] = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                continue
            self.__dict__[key] = kwargs[key]

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
