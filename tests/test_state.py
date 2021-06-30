#!/usr/bin/python3
'''Test for State'''


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State


class TestState(unittest.TestCase):
    '''Test class for State'''

    def test_intantiation(self):
        '''Testing when a new instance is created'''
        t1 = State()
        t2 = State(None)
        t3 = State("UwU")
        t4 = State({'I am': "Special"})
        t5 = State(["me", "gustan", "los", "memes"])
        self.assertTrue(isinstance(t1, State))
        self.assertTrue(type(t1), State)
        self.assertTrue(isinstance(t2, State))
        self.assertTrue(type(t2), State)
        self.assertTrue(isinstance(t3, State))
        self.assertTrue(type(t3), State)
        self.assertTrue(isinstance(t4, State))
        self.assertTrue(type(t4), State)
        self.assertTrue(isinstance(t5, State))
        self.assertTrue(type(t5), State)
    
    def test_sub_classes(self):
        '''Check if this class inherits from BaseModel'''
        self.assertTrue(issubclass(State, BaseModel))
        self.assertFalse(issubclass(State, FileStorage))
    
    def test_str(self):
        '''Testing str method'''
        inst = State()
        expected = "[State] ({}) {}".format(inst.id, inst.__dict__)
        str_out = inst.__str__()
        self.assertEqual(expected, str_out)
    
    def test_class_father_traits(self):
        '''Check if this subclass has the father attrs'''
        inst = State()
        self.assertTrue(hasattr(inst, "__init__"))
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

if (__file__ == "__main__"):
    unittest.main()
