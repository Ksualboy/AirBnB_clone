#!/usr/bin/python3
''' Executable command '''


import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    ''' Hbnb class command '''

    prompt = "(hbnb) "

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
        ''' Shows the string representatn '''
        if (len(args) == 0):
            print("** class name missing **")
            return
        
        prompt = args.split(' ')

        

    def do_destroy(self, args):
        ''' Deletes an instance based on the class name and id '''
        if (len(args) == 0):
            print("** class name missing **")
            return
        parts = args.split(' ')
        if (len(parts) == 1):
            print("awa")
        if (len(parts) == 2):
            print("ewe")
        return
        if (parts[1] != "BaseModel"):
            print("** class doesn't exist **")
        elif ():

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
