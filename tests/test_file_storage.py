#!/usr/bin/python3
'''Testing file storage'''


#!/usr/bin/python3
'''Test for base model'''


import unittest
import pep8
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''Test class for base model'''

    def test_intantiation(self):
        '''Testing when a new instance is created'''
        t1 = FileStorage()
        self.assertTrue(isinstance(t1, FileStorage))
        self.assertTrue(type(t1), FileStorage)
    
    def test_pep8(self):
        '''Testing pep8'''
        reP = pep8.StyleGuide().check_files(['models/engine/file_storage.py'])
        self.assertEqual(reP.total_errors, 0)

if (__file__ == "__main__"):
    unittest.main()

