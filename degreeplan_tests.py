import unittest

from UHCLdegreeplanner import *

class TestFunctions(unittest.TestCase):

    def test_isULC(self):
    '''Given a course, return True if the course is an upper-level CSCI or CENG course.
       isULC(course : str) -> bool
       Used to build the set constant ULC.
    '''
        self.assertTrue(isULC('CSCI 3456')) # Upper-level CSCI; doesn't need to be in COURSECATALOG for this function
        self.assertTrue(isULC('CSCI 4321')) # Upper-level CSCI
        self.assertTrue(isULC('CENG 3098')) # Upper-level CENG
        self.assertTrue(isULC('CENG 4765')) # Upper-level CENG

        # CSCI/CENG 5000+ courses are not in the CS B.S. degree program and are not considered
        
        self.assertFalse(isULC('CSCI 2325')) # 2000-level CSCI
        self.assertFalse(isULC('CSCI 1470')) # 1000-level CSCI
        self.assertFalse(isULC('CENG 2345')) # 2000-level CENG
        self.assertFalse(isULC('CENG 1079')) # 2000-level CENG
        self.assertFalse(isULC('MATH 1413')) # not CSCI or CENG; not upper-level
        self.assertFalse(isULC('PHYS 3001')) # not CSCI or CENG, but upper-level
        
        # Rubrics with lower-case characters will never be encountered because this function is only called once
        # with input from the set constant MAJOR_REQ (that is all upper-case).

    def test_prerequisites_met(self):
    '''Given a course and courses taken, return True if the course's prerequisites have been met.
       prerequisites_met(course : str, coursestaken : set) -> bool
    '''
        course = 'CSCI 1471' # Comp Sci II, prereqs are CSCI 1470 and MATH 2413
        coursestaken = {'CSCI 1470', 'HIST 1301', 'MATH 2413'} # prereqs are met!
        self.assertTrue(prerequisites_met(course, coursestaken))

        course = 'CSCI 1471' # Comp Sci II, prereqs are CSCI 1470 and MATH 2413
        coursestaken = {'CSCI 1470', 'HIST 1301', 'MATH 2320'} # prereqs NOT met
        self.assertFalse(prerequisites_met(course, coursestaken))

        course = 'WRIT 1301' # Composition I, no prerequisites
        coursestaken = {'CSCI 1470', 'HIST 1301', 'MATH 2320'} # coursestaken shouldn't matter
        self.assertTrue(prerequisites_met(course, coursestaken))

        course = 'HIST 1301' # U.S. History I, no prerequisites
        coursestaken = {} # coursestaken shouldn't matter
        self.assertTrue(prerequisites_met(course, coursestaken))
        
        


unittest.main()


# How to:
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
