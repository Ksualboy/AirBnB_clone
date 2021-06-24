#!/usr/bin/python3
''' Module with the file_storage class '''


import json
from os import path


class FileStorage:
    ''' Class for saving objects when the programm closes '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''
        return self.__objects
    
    def new(self, obj):
        ''' Sets a new obj into __objects '''
        self.__objects[obj.id] = obj

    def save(self):
        ''' Saves to the json file '''
        print("=========================")
        print(self.__objects)
        print("=========================")
        
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        ''' loads a json file to __objects '''
        if (not path.isfile(self.__file_path)):
            return
        # TODO: this doesn't work
        with open(self.__file_path, 'r') as file:
            self.__objects = dict(json.loads(file.read()))
