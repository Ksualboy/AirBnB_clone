#!/usr/bin/python3
'''Test for User'''


import unittest
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestState(unittest.TestCase):
    '''Test class for State'''

    def test_intantiation(self):
        '''Testing when a new instance is created'''
        t1 = User()
        t2 = User(None)
        t3 = User("UwU")
        t4 = User({'I am': "Special"})
        t5 = User(["me", "gustan", "los", "memes"])
        self.assertTrue(isinstance(t1, User))
        self.assertTrue(type(t1), User)
        self.assertTrue(isinstance(t2, User))
        self.assertTrue(type(t2), User)
        self.assertTrue(isinstance(t3, User))
        self.assertTrue(type(t3), User)
        self.assertTrue(isinstance(t4, User))
        self.assertTrue(type(t4), User)
        self.assertTrue(isinstance(t5, User))
        self.assertTrue(type(t5), User)
    
    def test_pep8(self):
        '''Testing pep8'''
        pep_res = pep8.StyleGuide().check_files(['models/user.py'])
        self.assertEqual(pep_res.total_errors, 0)

    def test_sub_classes(self):
        '''Check if this class inherits from BaseModel'''
        self.assertTrue(issubclass(User, BaseModel))
        self.assertFalse(issubclass(User, FileStorage))
    
    def test_str(self):
        '''Testing str method'''
        inst = User()
        expected = "[User] ({}) {}".format(inst.id, inst.__dict__)
        str_out = inst.__str__()
        self.assertEqual(expected, str_out)
    
    def test_class_father_traits(self):
        '''Check if this subclass has the father attrs'''
        inst = User()
        self.assertTrue(hasattr(inst, "__init__"))
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

if (__file__ == "__main__"):
    unittest.main()
