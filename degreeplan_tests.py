import unittest

from degreeplan_data import *      # imports catalog, corereq, and majorreq
from degreeplan_functions import * # import the functions


class TestFunctions(unittest.TestCase):

    def test_possibilities(self):
        
    
    # def prerequisites_met

    # def test_update_coursesneeded(self):
        coursesneeded = {'a', 'b', 'c'}
        coursestaken = {'b'}
        
        result = update_coursesneeded(coursesneeded, coursestaken)
        expectedresult = {'c', 'a'}
        self.assertEqual(result, expectedresult)
        


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
