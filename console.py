#!/usr/bin/python3
''' Executable command '''


import cmd
import json
import ast
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    ''' Hbnb class command '''

    prompt = "(hbnb) "
    __classes = {
        'BaseModel': BaseModel,
    }

    def do_create(self, args):
        ''' Creates an new instance of a class '''
        if (len(args) == 0):
            print("** class name missing **")
            return

        class_obj = self.class_check(args)
        if (class_obj == False):
            print("** class doesn't exist **")
            return

        new_instance = class_obj()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        ''' Shows the string representation '''
        obj = self.basic_checks(args)
        if (obj == False):
            return

        print(obj['obj'])

    def do_all(self, args):
        ''' Prints all instances based or not on the class name '''
        my_list = []
        objs = storage.all()

        if (args == ""):
            for key in objs:
                my_list.append(str(objs[key]))
            print(my_list)
            return

        class_name_arg = args.split(' ')[0]
        class_obj = self.class_check(class_name_arg)
        if (class_obj == False):
            print("** class doesn't exist **")
            return

        for key in objs:
            if (class_obj.__name__ == class_name_arg):
                my_list.append(str(objs[key]))

        print(my_list)

    def do_destroy(self, args):
        ''' Deletes an instance based on the class name and id '''
        obj = self.basic_checks(args)

        if (obj == False):
            return

        storage_obj = storage.all()
        del storage_obj[obj['args'][0] + '.' + obj['id']]
        self.update_json(storage_obj)


    def do_update(self, args):
        ''' Updates an object '''
        obj = self.basic_checks(args)
        if (obj == False):
            return

        if (len(obj['args']) == 2):
            print("** attribute name missing **")
            return
        elif (len(obj['args']) == 3):
            print("** value missing **")
            return

        setattr(obj['obj'], obj['args'][2], obj['args'][3])
        storage.new(obj['obj'])
        storage.save()


# 8=========> Our Tools <=========8

    def basic_checks(self, args):
        ''' Standarized error checks '''
        if (len(args) == 0):
            print("** class name missing **")
            return False

        parts = args.split(' ')

        class_obj = self.class_check(parts[0])
        if (class_obj == False):
            print("** class doesn't exist **")
            return False

        elif (len(parts) == 1):
            print("** instance id missing **")
            return False

        objs = storage.all()

        for key in objs:
            id = key.split('.')[1]
            if (id == parts[1]):
                return ({
                    'id': id,
                    'args': parts,
                    'obj': objs[key],
                    'class_obj': class_obj
                })

        print("** no instance found **")
        return False

    def class_check(self, class_name):
        ''' Checks if the class given exists '''
        if (class_name in self.__classes):
            return self.__classes[class_name]
        return False

    # DUDOSO si esto es valido xd
    def update_json(self, obj):
        ''' Overwrites the JSON file '''
        final_dict = {}
        for key in obj:
            final_dict[key] = obj[key].to_dict()
        with open("File.json", 'w') as f:
            json.dump(final_dict, f)
        storage.reload()

# 8===============================8

    def chequeo(self, args):
        ''' does the '''

    def do_quit(self, args):
        ''' Quit command '''
        exit()

    def help_quit(self):
        ''' Help for quit '''
        print("Quit command to exit the program\n")
    
    def do_EOF(self, args):
        ''' Exit command '''
        exit()
    
    def help_EOF(self):
        ''' Help for EOF '''
        print("EOF command to exit the program\n")
    
    def emptyline(self):
        ''' Empty line does nothing '''
        pass

    def do_xd(self, args):
        print("xd")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
