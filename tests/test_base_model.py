#!/usr/bin/python3
'''Test for base model'''


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''Test class for base model'''

    def test_intantiation(self):
        '''Testing when a new instance is created'''
        t1 = BaseModel()
        t2 = BaseModel(None)
        t3 = BaseModel("UwU")
        t4 = BaseModel({'I am': "Special"})
        t5 = BaseModel(["me", "gustan", "los", "memes"])
        self.assertTrue(isinstance(t3, BaseModel))
        self.assertTrue(type(t3), BaseModel)
    
    def test_save1(self):
        '''Testing save method'''
        dev = BaseModel()
        dev.name = "DreadZitoDev"
        dev.fav_game = "Fallout"
        dev.save()
        self.assertNotEqual(dev.created_at, dev.updated_at)
    
    def test_save2(self):
        '''Testing save method season 2'''
        tid = BaseModel()
        tid.name = "Isaac"
        tid.save()
        update1 = tid.updated_at

        tid.name = "Lazaro"
        tid.save()
        update2 = tid.updated_at

        tid.name = "Bethany"
        tid.save()
        update3 = tid.updated_at

        self.assertNotEqual(update1, update2)
        self.assertNotEqual(update1, update3)
    
    def test_to_dict(self):
        '''Testing to dict method'''
        vene = BaseModel()
        vene.name = "Dani_REP"
        vene.hungry = 100
        vene.save()
        vene_dict = vene.to_dict()
        self.assertEqual(vene_dict['id'], vene.id)
        self.assertEqual(vene_dict['created_at'],
        vene.created_at.isoformat())
        self.assertEqual(vene_dict['updated_at'],
        vene.updated_at.isoformat())
        self.assertEqual(vene_dict['name'], vene.name)
        self.assertEqual(vene_dict['hungry'], vene.hungry)
        self.assertEqual(vene_dict['__class__'], vene.__class__.__name__)
        self.assertTrue(isinstance(vene_dict, dict))

if (__file__ == "__main__"):
    unittest.main()
