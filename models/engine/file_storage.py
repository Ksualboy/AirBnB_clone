#!/usr/bin/python3
''' Module with the file_storage class '''


import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    ''' Class for saving objects when the programm closes '''

    __file_path = "File.json"
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''
        return self.__objects
    
    def new(self, obj):
        ''' Sets a new obj into __objects '''
        self.__objects[obj.to_dict()['__class__'] + "." + obj.id] = obj

    def save(self):
        ''' Saves to the json file '''
        mega_dict = {}

        for key in self.__objects:
            mega_dict[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(mega_dict, file)

    def reload(self):
        ''' loads a json file to __objects '''
        if (not path.isfile(self.__file_path)):
            return
        with open(self.__file_path, 'r') as file:
            self.__objects = dict(json.loads(file.read()))
            for key in self.__objects:
               self.__objects[key] = BaseModel(**self.__objects[key])
            print("me gusta el navo" + str(self.__objects))
