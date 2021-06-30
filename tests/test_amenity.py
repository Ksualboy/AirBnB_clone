#!/usr/bin/python3
'''Test for Amenity'''


import unittest
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestState(unittest.TestCase):
    '''Test class for State'''

    def test_intantiation(self):
        '''Testing when a new instance is created'''
        t1 = Amenity()
        t2 = Amenity(None)
        t3 = Amenity("UwU")
        t4 = Amenity({'I am': "Special"})
        t5 = Amenity(["me", "gustan", "los", "memes"])
        self.assertTrue(isinstance(t1, Amenity))
        self.assertTrue(type(t1), Amenity)
        self.assertTrue(isinstance(t2, Amenity))
        self.assertTrue(type(t2), Amenity)
        self.assertTrue(isinstance(t3, Amenity))
        self.assertTrue(type(t3), Amenity)
        self.assertTrue(isinstance(t4, Amenity))
        self.assertTrue(type(t4), Amenity)
        self.assertTrue(isinstance(t5, Amenity))
        self.assertTrue(type(t5), Amenity)
    
    def test_pep8(self):
        '''Testing pep8'''
        pep_res = pep8.StyleGuide().check_files(['models/amenity.py'])
        self.assertEqual(pep_res.total_errors, 0)

    def test_sub_classes(self):
        '''Check if this class inherits from BaseModel'''
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertFalse(issubclass(Amenity, FileStorage))
    
    def test_str(self):
        '''Testing str method'''
        inst = Amenity()
        expected = "[Amenity] ({}) {}".format(inst.id, inst.__dict__)
        str_out = inst.__str__()
        self.assertEqual(expected, str_out)
    
    def test_class_father_traits(self):
        '''Check if this subclass has the father attrs'''
        inst = Amenity()
        self.assertTrue(hasattr(inst, "__init__"))
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

if (__file__ == "__main__"):
    unittest.main()
