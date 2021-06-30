#!/usr/bin/python3
'''Test for City'''


import unittest
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.city import City


class TestState(unittest.TestCase):
    '''Test class for State'''

    def test_intantiation(self):
        '''Testing when a new instance is created'''
        t1 = City()
        t2 = City(None)
        t3 = City("UwU")
        t4 = City({'I am': "Special"})
        t5 = City(["me", "gustan", "los", "memes"])
        self.assertTrue(isinstance(t1, City))
        self.assertTrue(type(t1), City)
        self.assertTrue(isinstance(t2, City))
        self.assertTrue(type(t2), City)
        self.assertTrue(isinstance(t3, City))
        self.assertTrue(type(t3), City)
        self.assertTrue(isinstance(t4, City))
        self.assertTrue(type(t4), City)
        self.assertTrue(isinstance(t5, City))
        self.assertTrue(type(t5), City)
    
    def test_pep8(self):
        '''Testing pep8'''
        pep_res = pep8.StyleGuide().check_files(['models/city.py'])
        self.assertEqual(pep_res.total_errors, 0)

    def test_sub_classes(self):
        '''Check if this class inherits from BaseModel'''
        self.assertTrue(issubclass(City, BaseModel))
        self.assertFalse(issubclass(City, FileStorage))
    
    def test_str(self):
        '''Testing str method'''
        inst = City()
        expected = "[City] ({}) {}".format(inst.id, inst.__dict__)
        str_out = inst.__str__()
        self.assertEqual(expected, str_out)
    
    def test_class_father_traits(self):
        '''Check if this subclass has the father attrs'''
        inst = City()
        self.assertTrue(hasattr(inst, "__init__"))
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

if (__file__ == "__main__"):
    unittest.main()
