import unittest

from UHCLdegreeplanner import *

class TestFunctions(unittest.TestCase):

    def test_isULC(self):
        self.assertTrue(isULC('csci 3456'))
        self.assertTrue(isULC('CSCI 4000'))
        self.assertTrue(isULC('CENG 3000'))
        self.assertTrue(isULC('CENG 4000'))
        self.assertFalse(isULC('CSCI 2000'))
        self.assertFalse(isULC('CSCI 5000'))
        self.assertFalse(isULC('CENG 2000'))
        self.assertFalse(isULC('CENG 1000'))
    
        
# def isULC(course):
#     '''Given a course, return True if the course is an upper-level CSCI or CENG course.
#        isULC(course : str) -> bool
#        Used to build the set constant ULC
#     '''
#     isCSCI = course[:4] == 'CSCI'   # CSCI course?
#     isCENG = course[:4] == 'CENG'   # CENG course?
#     isULC = course[5] in ['3', '4'] # 3000 or 4000 level course?
#     return (isCSCI or isCENG) and isULC


unittest.main()

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
