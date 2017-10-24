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
