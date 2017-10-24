
from degreeplan_data import * # imports catalog, corereq, and majorreq


def prerequisites_met(course, coursestaken=coursestaken): # coursestaken could be removed because it is global
    '''Given a proposed course and a list of courses taken, 
       return True if the course's prerequisites have been met.
       prerequisites_met(course : str, coursestaken : set) -> bool
    '''
    prerequisites = requirements[course][1]     # get the set of prerequisites for the course
    return prerequisites.issubset(coursestaken) # is the set of prerequisites a subset of coursestaken?


def isULC(course):
    '''Given a course return True if the course is an upper-level CSCI or CENG course.
       isULC(course : str) -> bool
    '''
    isCSCI = course[:4] == 'CSCI'   # CSCI course?
    isCENG = course[:4] == 'CENG'   # CENG course?
    isULC = course[5] in ['3', '4'] # 3000 or 4000 level course?
    return (isCSCI or isCENG) and isULC


def LLCcomplete(coursestaken, LLC=LLC):
    '''Given a set of coursestaken and the set of LLC, return True if the LLC is complete.
       LLCcomplete(coursestaken : set, LLC : set) -> bool
    '''
    return LLC.issubset(coursestaken)
