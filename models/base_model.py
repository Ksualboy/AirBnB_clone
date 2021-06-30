#!/usr/bin/python3
''' Module with the base_model class '''


from datetime import datetime
import models
from uuid import uuid4


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
            models.storage.new(self)
            return

        for key in kwargs:
            if key == "__class__":
                continue
            if key == "created_at" or key == "updated_at":
                aux = kwargs[key]
                form = "%Y-%m-%dT%H:%M:%S.%f"
                self.__dict__[key] = datetime.strptime(aux, form)
                continue
            self.__dict__[key] = kwargs[key]

    def __str__(self):
        ''' Str representation of the instance '''
        cls_name = self.__class__.__name__
        s = "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
        return s

    def save(self):
        ''' Datetime last modification of object '''
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Dictionari representation of the instance '''
        ret_dict = self.__dict__.copy()
        ret_dict['__class__'] = self.__class__.__name__
        ret_dict['created_at'] = ret_dict['created_at'].isoformat()
        if ('updated_at' in ret_dict):
            ret_dict['updated_at'] = ret_dict['updated_at'].isoformat()
        return ret_dict
