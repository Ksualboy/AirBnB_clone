#!/usr/bin/python3
''' Module with the file_storage class '''


import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    ''' Class for saving objects when the programm closes '''

    __file_path = "File.json"
    __objects = {}
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
    }

    def all(self):
        ''' Returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' Sets a new obj into __objects '''
        if (type(obj) == dict and "set_null" in obj):
            ''' Handle the 'Destroy' case '''
            self.__objects[obj['id']] = obj['set_null']
        else:
            self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        ''' Saves to the json file '''
        mega_dict = {}

        for key in self.__objects:
            if (self.__objects[key] is not None):
                mega_dict[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(mega_dict, file)

    def reload(self):
        ''' loads a json file to __objects '''
        if (not path.isfile(self.__file_path)):
            return
        with open(self.__file_path, 'r') as file:
            aux_dict = dict(json.loads(file.read()))
            self.__objects.clear()
            for key in aux_dict:
                inst = aux_dict[key]['__class__']
                if (inst in self.__classes):
                    self.__objects[key] = self.__classes[inst](**aux_dict[key])
