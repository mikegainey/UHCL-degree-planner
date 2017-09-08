#!/usr/bin/python3

import sys
RED    = "\033[1;31m"  
BLUE   = "\033[1;34m"
CYAN   = "\033[1;36m"
GREEN  = "\033[0;32m"
RESET  = "\033[0;0m"
YELLOW = "\033[1;33m"  

# given a course, return the number of courses which that course will unlock
def prereq(course):
    count = 0
    for c,d in coursesneeded.items():
        remainingPrerequisites = d[1] - coursestaken
        a = course in remainingPrerequisites
        b = len(remainingPrerequisites) == 1
        if a and b:
            count += 1
    return count

degreeplan = []

terms = ['Fall 2017','Spring 2018', 'Fall 2018','Spring 2019', 'Fall 2019','Spring 2020',
         'Fall 2020','Spring 2021', 'Fall 2021','Spring 2022', 'Fall 2022','Spring 2023']

coursesneeded = {
        "MATH 2305":("Discrete Math (LLC)",{"MATH 2413"},'CSLLC'),
        "CSCI 1470":("Computer Science I (LLC)",set(),'CSLLC'),
        "PHYS 2325":("University Physics I (LLC)",{"MATH 2413"},'CSLLC'),
        "CSCI 1471":("Computer Science II (LLC)",{"CSCI 1470","MATH 2413"},'CSLLC'),
        "PHYS 2326":("University Physics II (LLC)",{"MATH 2414","PHYS 2325"},'CSLLC'),
        "MATH 2318":("Linear Algebra",{"MATH 2413"},''),
        "CSCI 2315":("Data Structures (LLC)",{"CSCI 1471"},'CSLLC'),
        "CENG 3312":("Digital Circuits & Lab",{"MATH 2414","PHYS 2326"},'CSULC'),
        "CSCI 3352":("Advanced Data Structures",{"CSCI 2315","MATH 2305","MATH 2414","PHYS 2325","PHYS 2326"},'CSULC'),
        "CSCI 3331":("Computer Organization & Assembly Language",{"CSCI 2315","MATH 2305","MATH 2414","PHYS 2325","PHYS 2326"},'CSULC'),
        "STAT 3334":("Probability & Statistics ...",{"MATH 2413","MATH 2414"},''),
        "CENG 3331":("Intro to Telecom and Neworks & Lab", {"CENG 3312"},'CSULC'),
        "CSCI 4333":("Design of Database Systems",{"CSCI 2315"},'CSULC'),
        "SWEN 4342":("Software Engineering",{"CSCI 1470","CSCI 2315"},''),
        "CSCI 3321":("Numerical Methods",{"MATH 2318","MATH 2320","CSCI 1471"},'CSULC'),
        "WRIT 3315":("Technical Writing",set(),''),
        "CENG 3351":("Computer Architecture & Lab (take with CSCI 4354)",{"CENG 3312"},'CSULC'),
        "CSCI 4354":("Operating Systems (take with CENG 3351)",{"CSCI 2315","CSCI 3331","MATH 2305","MATH 2414","PHYS 2325", 
                     "PHYS 2326"},'CSULC'),
        "CSCI 4388":("Senior Project in Computer Science",{"CSCI 3352","SWEN 4342"},'CSULC'),
        "CSCI 4320":("(elective) Web Application Development",{"CSCI 2315"},'CSULC'),
        "CSCI 4350":("(elective) Computer Graphics and Interface Design",{"MATH 2318", "MATH 2413"},'CSULC'),
        "CSCI 4362":("(elective) Computer Game Programming: Theory and Practice",{"CSCI 1470"},'CSULC'),
        "CSCI 4323":("(elective) Computer Security",{"CSCI 1471"},'CSULC')
        }

coursestaken = {"MATH 2413","MATH 2414", "MATH 2320"}
print()
term = 1

while True:

    print('=' * 40)
    semester = terms.pop(0)
    print(semester)
    term += 1
    print('=' * 40)

    # for any courses that have been taken, remove them from coursesneeded
    for c in coursestaken:
        if c in coursesneeded:
            del coursesneeded[c]

    # check to see if all CS Lower Level Core (CSLLC) courses have been completed
    LLCcomplete = True
    for c in coursesneeded:
        if coursesneeded[c][2] == 'CSLLC':
            LLCcomplete = False
            break

    # list courses for which prerequisites have been met
    choices = []
    for c,d in coursesneeded.items():
        prereqComplete = len(d[1] - coursestaken) == 0
        LLCtest = not (d[2] == 'CSULC' and LLCcomplete == False)
        if prereqComplete and LLCtest:
            pre = prereq(c)
            if pre > 0:
                sys.stdout.write(BLUE)
            if d[2] == 'CSLLC':
                sys.stdout.write(GREEN)
            print("{}) (unlocks {} courses) {} {}".format(len(choices)+1,pre,c,d[0]))
            sys.stdout.write(RESET)
            choices.append(c)

    if len(coursesneeded) <= 2:
        for c,d in coursesneeded.items():
            degreeplan.append([semester, c, d[0]])
        print("\n... and you're done!\n")
        break

    new1 = int(input("\nEnter the first course to take:  "))-1
    new2 = int(input("Enter the second course to take: "))-1
    print()
    sys.stdout.write(YELLOW)
    print("{} --> {} {}".format(semester, choices[new1], coursesneeded[choices[new1]][0]))
    print("{} --> {} {}".format(semester, choices[new2], coursesneeded[choices[new2]][0]))
    sys.stdout.write(RESET)
    degreeplan.append([semester, choices[new1], coursesneeded[choices[new1]][0]])
    degreeplan.append([semester, choices[new2], coursesneeded[choices[new2]][0]])
    coursestaken.update([choices[new1],choices[new2],])
    print()

# =============== after break =================
# print degree plan summary
print()
for c in range(len(degreeplan)):
    print("{:12} {:9} {}".format(degreeplan[c][0], degreeplan[c][1], degreeplan[c][2]))
    if c % 2 == 1:
        print()
print("\n")


# future changes
# don't allow electives to show up until 3rd year
