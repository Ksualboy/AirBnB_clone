#!/usr/bin/python3
'''Testing file storage'''


#!/usr/bin/python3
'''Test for base model'''


import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''Test class for base model'''

    def test_intantiation(self):
        '''Testing when a new instance is created'''
        t1 = FileStorage()
        t2 = FileStorage(None)
        t3 = FileStorage("UwU")
        t4 = FileStorage({'I am': "Special"})
        t5 = FileStorage(["me", "gustan", "los", "memes"])
        self.assertTrue(isinstance(t3, FileStorage))
        self.assertTrue(type(t3), FileStorage)
    
    def test_ids(self):
        '''Test if id is unique'''
        random = FileStorage()
        other_random = FileStorage()
        self.assertNotEqual(random.id, other_random.id)

    def test_save1(self):
        '''Testing save method'''
        dev = FileStorage()
        dev.name = "DreadZitoDev"
        dev.fav_game = "Fallout"
        dev.save()
        self.assertNotEqual(dev.created_at, dev.updated_at)
    
    def test_save2(self):
        '''Testing save method season 2'''
        tid = FileStorage()
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
        vene = FileStorage()
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

