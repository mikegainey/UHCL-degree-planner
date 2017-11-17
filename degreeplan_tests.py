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
        
        # Course numbers with lower-case characters will never be encountered because this function is only called once
        # with input from the set constant MAJOR_REQ (that is all upper-case).


    def test_prerequisites_met(self):
        '''Given a course and courses taken, return True if the course's prerequisites have been met.
           prerequisites_met(course : str, coursestaken : set) -> bool
        '''
        course = 'CSCI 1471' # Comp Sci II, prereqs are CSCI 1470 and MATH 2413
        coursestaken = {'CSCI 1470', 'HIST 1301', 'MATH 2413'} # prereqs are met!
        self.assertTrue(prerequisites_met(course, coursestaken))

        course = 'CSCI 1471' # Comp Sci II, prereq is CSCI 1470
        coursestaken = {'HIST 1301', 'MATH 2320'} # prereqs NOT met
        self.assertFalse(prerequisites_met(course, coursestaken))

        course = 'WRIT 1301' # Composition I, no prerequisites
        coursestaken = {'CSCI 1470', 'HIST 1301', 'MATH 2320'} # coursestaken shouldn't matter
        self.assertTrue(prerequisites_met(course, coursestaken))

        course = 'HIST 1301' # U.S. History I, no prerequisites
        coursestaken = {} # coursestaken shouldn't matter
        self.assertTrue(prerequisites_met(course, coursestaken))
        

    def test_LLCcomplete(self):
        '''Given the set of courses taken, return True if the CS LLC is complete.
           LLCcomplete(coursestaken : set) -> bool
           LLC = {'CSCI 1470', 'CSCI 1471', 'CSCI 2315', 'PHYS 2325', 'PHYS 2326', 
                  'MATH 2413', 'MATH 2414', 'MATH 2305', 'WRIT 1301'}
        '''
        coursestaken = {'CSCI 1470', 'CSCI 1471', 'CSCI 2315', 'PHYS 2325', 'PHYS 2326', # LLC is all there
                        'MATH 2413', 'MATH 2414', 'MATH 2305', 'WRIT 1301', 'POLS 2305', # + 1 other course
                        'PHYS 2125', 'PHYS 2126'} # labs were added to LLC
        self.assertTrue(LLCcomplete(coursestaken))

        coursestaken = {'CSCI 1470', 'CSCI 1471', 'CSCI 2315', 'PHYS 2325', 'PHYS 2326', # LLC is missing 'WRIT 1301'
                        'MATH 2413', 'MATH 2414', 'HIST 1302', 'MATH 2305', 'POLS 2305', # HIST and POLS also included
                        'PHYS 2125', 'PHYS 2126'} 
        self.assertFalse(LLCcomplete(coursestaken))


    def test_getChoices(self):
        '''Given the set of courses taken, return the set of courses eligible to be taken (choices)
        getChoices(coursestaken : set) -> 
        I don't know how to exhaustively test this function!
        '''
        coursestaken = set() # a new student
        choices = UNI_CORE | MAJOR_REQ | LANG_PHIL_CULTURE | CREATIVE_ARTS | SOCIAL_SCIENCE - ULC
        # the next line removes courses for which prerequisites are not met
        choices = {course for course in choices if prerequisites_met(course, coursestaken)}
        choices -= {'PHYS 2125', 'PHYS 2126', 'CENG 3112', 'CENG 3131'} # labs don't have prereqs, but still can't be taken
        self.assertEqual(getChoices(coursestaken), choices)

        coursestaken = {'PSYC 1100'} # just took one course
        choices = UNI_CORE | MAJOR_REQ | LANG_PHIL_CULTURE | CREATIVE_ARTS | SOCIAL_SCIENCE - ULC
        choices = {course for course in choices if prerequisites_met(course, coursestaken)}
        choices -= {'PHYS 2125', 'PHYS 2126', 'CENG 3112', 'CENG 3131'} # labs don't have prereqs, but still can't be taken
        choices -= {'PSYC 1100'} # this is no longer a choice
        self.assertEqual(getChoices(coursestaken), choices)
        
        # verify that taking Intro to Philosophy removes all lang/phil/culture courses from choices
        coursestaken = {'PHIL 1301'}
        choices = UNI_CORE | MAJOR_REQ | CREATIVE_ARTS | SOCIAL_SCIENCE - ULC 
        choices = {course for course in choices if prerequisites_met(course, coursestaken)}
        choices -= {'PHYS 2125', 'PHYS 2126', 'CENG 3112', 'CENG 3131'} # labs don't have prereqs, but still can't be taken
        self.assertEqual(getChoices(coursestaken), choices)

        # verify that taking Arts and the Child removes all creative arts courses from choices
        coursestaken = {'ARTS 2379'}
        choices = UNI_CORE | MAJOR_REQ | LANG_PHIL_CULTURE | SOCIAL_SCIENCE - ULC 
        choices = {course for course in choices if prerequisites_met(course, coursestaken)}
        choices -= {'PHYS 2125', 'PHYS 2126', 'CENG 3112', 'CENG 3131'} # labs don't have prereqs, but still can't be taken
        self.assertEqual(getChoices(coursestaken), choices)

        # verify that taking Macroeconomics removes all social/behavioral science courses from choices
        coursestaken = {'ECON 2301'}
        choices = UNI_CORE | MAJOR_REQ | LANG_PHIL_CULTURE | CREATIVE_ARTS - ULC 
        choices = {course for course in choices if prerequisites_met(course, coursestaken)}
        choices -= {'PHYS 2125', 'PHYS 2126', 'CENG 3112', 'CENG 3131'} # labs don't have prereqs, but still can't be taken
        self.assertEqual(getChoices(coursestaken), choices)
        
        # LLC is complete; ULC are now choices (electives require junior standing; CSCI 4354 requires senior standing)
        coursestaken = {'CSCI 1470', 'CSCI 1471', 'CSCI 2315', 'PHYS 2325', 'PHYS 2326', # LLC is complete
                        'MATH 2413', 'MATH 2414', 'MATH 2305', 'WRIT 1301', 'PHYS 2125', 'PHYS 2126'}
        choices = UNI_CORE | MAJOR_REQ | LANG_PHIL_CULTURE | CREATIVE_ARTS | SOCIAL_SCIENCE | ELECTIVES
        choices = {course for course in choices if prerequisites_met(course, coursestaken)}
        choices -= coursestaken # remove courses taken from choices
        choices -= (ELECTIVES | REQ_SENIOR) # remove courses that require junior & senior standing
        choices -= {'CENG 3131'} # labs don't have prereqs, but still can't be taken unless the main course can
        self.assertEqual(getChoices(coursestaken), choices)

        # test that junior standing unlocks electives and WRIT 3315
        coursestaken = {'WRIT 1301', 'WRIT 1302', 'MATH 2413', 'PHYS 2325', 'PHYS 2326', 'HIST 1301', 'HIST 1302', # 22
                        'POLS 2305', 'POLS 2306', 'PSYC 1100', 'PHIL 1301', 'ARTS 1303', 'ECON 2301',              # 16
                        'CSCI 1470', 'CSCI 1471', 'CSCI 2315', 'MATH 2414', 'MATH 2305',                           # 18
                        'PHYS 2125', 'PHYS 2126'} # and LLC complete                                               #  2
        self.assertEqual(classification(coursestaken), ('sophomore', 58)) # sophomore with 58 hours
        self.assertTrue(LLCcomplete(coursestaken))                        # LLC is complete (needed to take electives)

        # choices should not include courses that require junior standing
        choices = getChoices(coursestaken)
        self.assertFalse('CSCI 33x1' in choices) # electives are taken in the junior or senior year
        self.assertFalse('WRIT 3315' in choices) # WRIT 3315 requires junior standing

        # add one course to attain junior standing
        coursestaken.add('COMM 1315')
        self.assertEqual(classification(coursestaken), ('junior', 61)) # junior with 61 hours
        choices = getChoices(coursestaken)
        self.assertTrue('CSCI 33x1' in choices) # electives are taken in the junior or senior year
        self.assertTrue('WRIT 3315' in choices) # WRIT 3315 requires junior standing

        # test that senior standing unlocks CSCI 4354; corequisites (CENG ...) also need to be choices
        coursestaken |= {'CHEM 1311', 'MATH 2318', 'MATH 2320', 'STAT 3334', 'CSCI 3331', 'CSCI 3352', 'CSCI 4333', # 21
                         'CSCI 3321', 'SWEN 4342', 'CHEM 1111'}                                                     #  7
        self.assertEqual(classification(coursestaken), ('junior', 89)) # junior with 89 hours

        # choices should not include courses that require senior standing
        choices = getChoices(coursestaken)
        self.assertFalse('CSCI 4354' in choices) # can't take CSCI 4354; requires senior standing

        # add one course to attain senior standing
        coursestaken.add('WRIT 3315')
        self.assertEqual(classification(coursestaken), ('senior', 92)) # senior with 92 hours
        choices = getChoices(coursestaken)
        self.assertTrue('CSCI 4354' in choices) # can now take CSCI 4354 
        
        # The next test tests the set comprehension: choices = {course for course in choices if ...}
        
        
    def test_prereq_comprehension(self):
        '''This tests the one-liner set comprehension that takes a set of coureses and filters out courses
           with unmet prerequisites:
           choices = {course for course in choices if prerequisites_met(course, coursestaken)}
        '''
        coursestaken = set() # only coureses with no prerequisites can be taken
        choices = {'CSCI 1470', 'CSCI 1471'} # CSCI 1471 has prerequisites (CSCI 1470 and MATH 2413)
        choices = {course for course in choices if prerequisites_met(course, coursestaken)}
        self.assertEqual(choices, {'CSCI 1470'}) # only CSCI 1470 should make it through

        coursestaken = {'CSCI 1470', 'MATH 2413'}
        choices = {'CSCI 1471', 'CSCI 2315'} # CSCI 1471 prereqs are met; CSCI 2315 prereqs NOT met
        choices = {course for course in choices if prerequisites_met(course, coursestaken)}
        self.assertEqual(choices, {'CSCI 1471'}) # only CSCI 1471 should make it through


    def test_isCourseNumber(self):
        '''Given a string, return True if the string consists of 4 alpha + ' ' + 4 decimal characters
           isCourseNumber(maybeCourseNumber : str) -> bool
           the alpha characters can be uppercase or lowercase
        '''
        self.assertFalse(isCourseNumber('CompSci 1470')) # length > 9 characters
        self.assertFalse(isCourseNumber('CSCI 147')) # length < 9 characters
        self.assertFalse(isCourseNumber('CSCI_1470')) # only 1 word
        self.assertFalse(isCourseNumber('CS 1 1470')) # 3 words
        self.assertFalse(isCourseNumber('CSC1 1470')) # first word is not all alphabetic
        self.assertFalse(isCourseNumber('CSCI 1A70')) # second word is not all decimal
        self.assertFalse(isCourseNumber('CSC 147  ')) # first and second words not of length 4

        # checking that a course applies to degree requirements is performed in add2CoursesTaken
        self.assertTrue(isCourseNumber('asdf 1234')) # conforms to the correct format; 


    def test_extractCourseNumbers(self):
        '''Given a list of lines from a file, return an ordered list of valid course numbers.
        extractCourseNumbers(lines : [str]) -> [str]
        These course numbers might not apply to the CS BS degree (checked in add2CoursesTaken)
        '''
        lines = ['CSCI 1470\n',
                 'CSCI 1471 Computer Science II\n',
                 'phys 2325 lowercase course numbers are ok\n', # lowercase is ok here
                 'qwer 1234 this is converted to upper but not filtered out yet (not until add2CoursesTaken)',
                 'This is not a course and should be ignored\n',
                 '\n', # a blank line
                 'math 2314']
        self.assertEqual(extractCourseNumbers(lines), ['CSCI 1470', 'CSCI 1471', 'PHYS 2325', 'QWER 1234', 'MATH 2314'])


    def test_add2CoursesTaken(self):
        '''Add a course to coursestaken only if it applies to the CS BS degree
           add2CoursesTaken(course : str, coursestaken : set) -> NoneType (+ mutating coursestaken, screen output)
           used twice in getCoursesTaken (so this function prevents code duplication)
           the course parameter must be uppercase (done in extractCourseNumbers and getCoursesTaken)
        '''
        coursestaken = set()

        course = 'CSCI 1470' # valid course number and degree requirement
        add2CoursesTaken(course, coursestaken) # try to add CSCI 1470 to coursestaken
        self.assertTrue(course in coursestaken) # see if it worked (it should)

        course = 'CSCI 1234' # valid course number but not a degree requirement
        add2CoursesTaken(course, coursestaken) # try to add CSCI 1234 to coursestaken
        self.assertFalse(course in coursestaken) # see if it worked (it should not)


    # getCoursesTaken - test manually because of user input prompts
    # getTerm - test manually because of user input prompts
        

    def test_incTerm(self):
        '''Given a current term, return the next term
           incTerm(currentTerm : str) -> str
           This function will produce a runtime error
           if term's fist word is not in seasons (but that should never happen).
        '''
        self.assertEqual(incTerm('Fall 2017'), 'Spring 2018') # Spring 2018 follows Fall 2017
        self.assertEqual(incTerm('Spring 2018'), 'Summer 2018') # Summer 2018 follows Spring 2018
        self.assertEqual(incTerm('Summer 2018'), 'Fall 2018') # Fall 2018 follows Summer 2018
        

    def test_prereqFor(self):
        '''Given a course, return the number of (still needed) courses for which that course is a prerequisite
           prereqFor(course : str, coursestaken : set) -> int
        '''
        coursestaken = set()
        self.assertEqual(prereqFor('MATH 2413', coursestaken), 5) # prereq for PHYS 2325, MATH 2305, MATH 2318,
                                                                  #            MATH 2414, STAT 3334

        self.assertEqual(prereqFor('WRIT 1301', coursestaken), 3) # prereq for WRIT 1302, LITR 2341, & WRIT 3315
        coursestaken.add('PHIL 1301') # now LITR 2341 doesn't count as a course for which WRIT 1301 is a prerequisite
        self.assertEqual(prereqFor('WRIT 1301', coursestaken), 2) # prereq for WRIT 1302 & WRIT 3315 (not LITR 2341)
        # note: this is the only case where the prereqFor number will change


    def test_classification(self):
        '''Given coursestaken, return a tuple with (classification, total hours completed) where classification is ...
           freshman for 1-29 hours, sophomore for 30-59 hours, junior for 60-89 hours, and senior for 90+ hours
           classificaiton(coursestaken : set) -> (str, int)
        '''
        coursestaken = set()
        self.assertEqual(classification(coursestaken), ('freshman', 0))

        coursestaken = {'WRIT 1301', 'WRIT 1302', 'MATH 2413', 'PHYS 2325', 'PHYS 2125',
                        'PHYS 2326', 'PHYS 2126', 'HIST 1301', 'HIST 1302', 'POLS 2305'}
        self.assertEqual(classification(coursestaken), ('freshman', 27))

        coursestaken.add('POLS 2306')
        self.assertEqual(classification(coursestaken), ('sophomore', 30))

        coursestaken |= {'COMM 1315', 'PSYC 1100', 'CHEM 1311', 'CHEM 1111', 'MATH 2305',
                         'MATH 2318', 'MATH 2414', 'MATH 2320', 'STAT 3334', 'CSCI 1470'}
        self.assertEqual(classification(coursestaken), ('sophomore', 58))

        coursestaken.add('CSCI 1471')
        self.assertEqual(classification(coursestaken), ('junior', 62))

        coursestaken |= {'CSCI 3331', 'CSCI 2315', 'CSCI 3352', 'CSCI 4333', 'CSCI 3321', 'CSCI 4354',
                         'CENG 3312', 'CENG 3112', 'CENG 3331', 'CENG 3131'}
        self.assertEqual(classification(coursestaken), ('junior', 88))

        coursestaken |= {'CENG 3351', 'CENG 3151'}
        self.assertEqual(classification(coursestaken), ('senior', 92))

        coursestaken |= {'SWEN 4342', 'WRIT 3315', 'CSCI 4388', 'WGST 1301', 'ARTS 1304', 'SOCI 1301', 'CSCI 33x1', 'CSCI 33x2',
                         'CSCI 33x3', 'CSCI 32xx'}
        self.assertEqual(classification(coursestaken), ('senior', 121))

        
    def test_displayChoices(self):
        '''Given a set of course choices, display and return a choice dictionary (menu)
           displayChoices(term : str, choices : set, coursestaken : set) -> {index: course}
        '''
        # the order of courseMenu is sorted by category, then by course number
        term = 'Fall 2017'
        coursestaken = set()
        
        choices = {'PHIL 1301', 'ARTS 1303', 'ECON 2301', }
        choices |= {'PSYC 1100', 'WRIT 1302'} # uni_core
        choices |= {'CSCI 1470', 'WRIT 1301'} # LLC
        choices |= {'CHEM 1311', 'CSCI 4388'} # major_req
        choices |= {'CSCI 32xx', 'CSCI 33x1'} # electives
        menu = {1 : 'PHIL 1301', 2 : 'ARTS 1303', 3 : 'ECON 2301', 4 : 'PSYC 1100', 5 : 'WRIT 1302',
                6 : 'CSCI 1470', 7 : 'WRIT 1301', 8 : 'CHEM 1311', 9 : 'CSCI 4388', 10 : 'CSCI 32xx', 11 : 'CSCI 33x1'}

        self.assertEqual(displayChoices(term, choices, coursestaken), menu)


    def test_checkCorequisites(self):
        '''Given a list of courses chosen for a term, return a list of tuples: (course, {set of unselected corequisite(s)} )
           representing courses and their unselected corequisites; The course is listed only if there are unselected corequisites.
           checkCorequisites(courses : [str]) -> [(str, {set of str})]
        '''
        courses = ['CSCI 1470', 'PHYS 2325', 'PHYS 2125'] # corequisite requirements met
        self.assertEqual(checkCorequisites(courses), [])

        courses = ['CSCI 1470', 'PHYS 2325'] # PHYS 2325 needs the lab, PHYS 2125 
        self.assertEqual(checkCorequisites(courses), [('PHYS 2325', {'PHYS 2125'})])

        courses = ['CENG 3351', 'CSCI 1470'] # CENG 3351 needs the lab (CENG 3151) and CSCI 4354
        self.assertEqual(checkCorequisites(courses), [('CENG 3351', {'CENG 3151', 'CSCI 4354'})])

        
unittest.main(buffer=True) # buffer=True suppresses output of print statements in functions
