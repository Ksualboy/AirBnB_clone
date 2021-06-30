#!/usr/bin/python3
'''Test for the console'''


import unittest
import pep8
from console import HBNBCommand


class ConsoleTest(unittest.TestCase):
    '''Test class for the main concole'''

    def test_obj_creation(self):
        '''Test when an object is created'''
