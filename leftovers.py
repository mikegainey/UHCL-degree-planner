coursestaken = set()

# this doesn't include language, creative arts, and social science courses because there are options

def update_coursesneeded(coursesneeded, coursestaken):
    '''For any courses that have been taken, remove them from coursesneeded
       update_coursesneeded(coursesneeded : set, coursestaken : set) -> set
    '''

    # a - b removes elements in b from a; returns a new list (does not mutate coursesneeded)
    coursesneeded -= coursestaken

    return coursesneeded


# function: determine if LLC is complete
def LLCcomplete(coursestaken):
    


# check to see if all CS Lower Level Core (CSLLC) courses have been completed
# LLCcomplete = True
# for c in coursesneeded:
#     if coursesneeded[c][2] == 'CSLLC':
#         LLCcomplete = False
#         break

#####

import unittest

from degreeplan_data import * 


coursestaken = set()

# this doesn't include language, creative arts, and social science courses because there are options
coursesneeded = corereq | majorreq # the intersection of corereq and majorreq

degreeplan = []

#####


coursesneeded = {'a', 'b', 'c'}
coursestaken = {'b'}


def update_coursesneeded(coursesneeded, coursestaken):
    '''For any courses that have been taken, remove them from coursesneeded
       coursesneeded and coursestaken are sets
    '''
    print("Updating courses needed ...")

    # a - b removes elements in b from a; returns a new list (does not mutate coursesneeded)
    coursesneeded -= coursestaken
    return coursesneeded

print("coursesneeded = {}".format(coursesneeded))
coursesneeded = update_coursesneeded(coursesneeded, coursestaken)
print("coursesneeded = {}".format(coursesneeded))

=====

from degreeplan_data import * # import the course catalog, corereq, majorreq, and LLC

coursestaken = {'MATH 2413', 'CSCI 1470'}

# this doesn't include language, creative arts, and social science courses because there are options
coursesneeded = corereq | majorreq # the intersection of corereq and majorreq
coursesneeded = coursesneeded - coursestaken

degreeplan = []


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

    
# Print a list of courses than can be taken
# - prerequisites met
# - LLC complete (if needed)
# - TODO: add language, creative arts, and social science courses

def listchoices(coursestaken, requirements=requirements, LLC=LLC):
    '''Given the sets of coursestaken, requirements, and LLC, return a list of courses that can be taken
       listchoices( coursestaken : set, requirements : set, LLC : set) -> [str]
    '''
    choices = coursesneeded
    if not LLCcomplete(coursestaken, LLC):
        # choices = choices - (upper level courses) # make a ULC constant
    print(LLC)
    for course in requirements:
        p = prerequisites_met(course, coursestaken)
        ul = isULC(course, requirements)
        llc = LLCcomplete(coursestaken, LLC)
        # print("course = {}, p = {:2}, UL = {:2}, LLC = {:2}".format(course, p, ul, llc))
        if p and (not ul or llc):
            choices.append(course)
    return choices

listchoices(coursestaken)
