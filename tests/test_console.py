#!/usr/bin/python3
'''Test for the console'''


import unittest
import cmd
import pep8
from console import HBNBCommand


class ConsoleTest(unittest.TestCase):
    '''Test class for the main concole'''

    def test_obj_creation(self):
        '''Test when an object is created'''
        self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        self.assertFalse(HBNBCommand().onecmd("create City"))
        self.assertFalse(HBNBCommand().onecmd("create User"))
        self.assertFalse(HBNBCommand().onecmd("create State"))
        self.assertFalse(HBNBCommand().onecmd("create Review"))

    def test_pep8(self):
        '''Testing pep8'''
        pep_res = pep8.StyleGuide().check_files(['console.py'])
        self.assertEqual(pep_res.total_errors, 0)