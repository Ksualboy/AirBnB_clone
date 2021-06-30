#!/usr/bin/python3
'''Test for State'''


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place


class TestState(unittest.TestCase):
    '''Test class for State'''

    def test_intantiation(self):
        '''Testing when a new instance is created'''
        t1 = Place()
        t2 = Place(None)
        t3 = Place("UwU")
        t4 = Place({'I am': "Special"})
        t5 = Place(["me", "gustan", "los", "memes"])
        self.assertTrue(isinstance(t1, Place))
        self.assertTrue(type(t1), Place)
        self.assertTrue(isinstance(t2, Place))
        self.assertTrue(type(t2), Place)
        self.assertTrue(isinstance(t3, Place))
        self.assertTrue(type(t3), Place)
        self.assertTrue(isinstance(t4, Place))
        self.assertTrue(type(t4), Place)
        self.assertTrue(isinstance(t5, Place))
        self.assertTrue(type(t5), Place)
    
    def test_sub_classes(self):
        '''Check if this class inherits from BaseModel'''
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertFalse(issubclass(Place, FileStorage))
    
    def test_str(self):
        '''Testing str method'''
        inst = Place()
        expected = "[Place] ({}) {}".format(inst.id, inst.__dict__)
        str_out = inst.__str__()
        self.assertEqual(expected, str_out)
    
    def test_class_father_traits(self):
        '''Check if this subclass has the father attrs'''
        inst = Place()
        self.assertTrue(hasattr(inst, "__init__"))
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

if (__file__ == "__main__"):
    unittest.main()
