#!/usr/bin/python3
'''Test for State'''


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.review import Review


class TestState(unittest.TestCase):
    '''Test class for State'''

    def test_intantiation(self):
        '''Testing when a new instance is created'''
        t1 = Review()
        t2 = Review(None)
        t3 = Review("UwU")
        t4 = Review({'I am': "Special"})
        t5 = Review(["me", "gustan", "los", "memes"])
        self.assertTrue(isinstance(t1, Review))
        self.assertTrue(type(t1), Review)
        self.assertTrue(isinstance(t2, Review))
        self.assertTrue(type(t2), Review)
        self.assertTrue(isinstance(t3, Review))
        self.assertTrue(type(t3), Review)
        self.assertTrue(isinstance(t4, Review))
        self.assertTrue(type(t4), Review)
        self.assertTrue(isinstance(t5, Review))
        self.assertTrue(type(t5), Review)
    
    def test_sub_classes(self):
        '''Check if this class inherits from BaseModel'''
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertFalse(issubclass(Review, FileStorage))
    
    def test_str(self):
        '''Testing str method'''
        inst = Review()
        expected = "[Review] ({}) {}".format(inst.id, inst.__dict__)
        str_out = inst.__str__()
        self.assertEqual(expected, str_out)
    
    def test_class_father_traits(self):
        '''Check if this subclass has the father attrs'''
        inst = Review()
        self.assertTrue(hasattr(inst, "__init__"))
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

if (__file__ == "__main__"):
    unittest.main()
