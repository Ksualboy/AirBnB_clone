#!/usr/bin/python3
''' Executable command '''


import cmd
import json
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

        elif (args == "BaseModel"):
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        ''' Shows the string representation '''
        obj = self.basic_checks(args)
        if (obj == False):
            return

        print(obj['obj'])
    
    def do_all(self, args):
        ''' Prints all instances based or not on the class name '''
        parts = args.split(' ')
        if (parts[0] != "BaseModel"):
            print("** class doesn't exist **")
            return
        my_list = []
        objs = storage.all()
        for key in objs:
            my_list.append(str(objs[key]))
        print(my_list)
        

    def do_destroy(self, args):
        ''' Deletes an instance based on the class name and id '''
        obj = self.basic_checks(args)

        if (obj == False):
            return

        final_dict = {}
        storage_obj = storage.all()
        del storage_obj[obj['args'][0] + '.' + obj['id']]
        for key in storage_obj:
            final_dict[key] = storage_obj[key].to_dict()
        with open("File.json", 'w') as f:
            json.dump(final_dict, f)
        storage.reload()

    
    def do_update(self, args):
        ''' Updates an object '''
        obj = self.basic_checks(args)
        if (obj == False):
            return

        # if (len(obj[args]))
        
            
# 8=========> Our Tools <=========8
    
    def basic_checks(self, args):
        ''' Standarized error checks '''
        if (len(args) == 0):
            print("** class name missing **")
            return False
        parts = args.split(' ')
        if (parts[0] != "BaseModel"):
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
                    'obj': objs[key]
                })

        print("** no instance found **")
        return False
    
    def class_check(self, class_name):
        for key, value in HBNBCommand.__class.items():
            if (key == class_name):
                return value
        
        return False

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
