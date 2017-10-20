# The UHCL undergraduate catalog can be found at the following URL:
# https://www.uhcl.edu/academics/resources/catalog/documents/2016-2017-undergrad-catalog.pdf

# coursecatalog is a dictionary; the key is a course rubric, 'PHYS 2325'
#   the value is a tuple, consisting of
#   - the full title of the course, 'University Physics I'
#   - a set of prerequisites, {'MATH 2413'}
#   - a flag: CSLLC, CSULC, or ''

coursecatalog = {
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


corereq = ['WRIT 1301', 'WRIT 1302', 'MATH 2413', 'PHYS 2325', 'PHYS 2326', 'HIST 1301', 'HIST 1302',
           'POLS 2305', 'POLS 2306', 'COMM 1315', 'PSYC 1100', 'PHYS 2125', 'PHYS 2126']

majorreq = ['CHEM 1311', 'CHEM 1111', 'MATH 2305', 'MATH 2318', 'MATH 2414', 'MATH 2320', 'STAT 3334',
            'CSCI 1470', 'CSCI 1471', 'CSCI 3331', 'CSCI 2315', 'CSCI 3352', 'CSCI 4333', 'CSCI 3321',
            'CSCI 4354', 'CENG 3312', 'CENG 3331', 'CENG 3351', 'SWEN 4342', 'WRIT 3315', 'CSCI 4388']

# note: Decide how to display CENG classes with lab, and also PHYS courses with lab (currently inconsistent)
# Should I count labs as separate courses? (no, because they need to stay coupled with the main course).

################################################################################
# function: build courses needed from degree requirements
# - this will not include language, creative arts, and social science courses because there are options

################################################################################
# function: remove courses taken from courses needed

################################################################################
# functions: if complete, stop showing them in the available courses list
# - language complete?
# - creative arts complete?
# - social science complete?
# 

################################################################################
# function: determine if LLC is complete

################################################################################
# function: list courses that can be taken
# - prerequisites complete
# - LLC complete if needed
# - show electives only after LLC complete



# given a course, return the number of courses which that course will unlock
# def prereq(course):
#     count = 0
#     for c,d in coursesneeded.items():
#         remainingPrerequisites = d[1] - coursestaken
#         a = course in remainingPrerequisites
#         b = len(remainingPrerequisites) == 1
#         if a and b:
#             count += 1
#     return count

degreeplan = []

terms = ['Fall 2017','Spring 2018', 'Fall 2018','Spring 2019', 'Fall 2019','Spring 2020',
         'Fall 2020','Spring 2021', 'Fall 2021','Spring 2022', 'Fall 2022','Spring 2023']


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
    # for c in coursestaken:
    #     if c in coursesneeded:
    #         del coursesneeded[c]

    # check to see if all CS Lower Level Core (CSLLC) courses have been completed
    # LLCcomplete = True
    # for c in coursesneeded:
    #     if coursesneeded[c][2] == 'CSLLC':
    #         LLCcomplete = False
    #         break

    # list courses for which prerequisites have been met
    # choices = []
    # for c,d in coursesneeded.items():
    #     prereqComplete = len(d[1] - coursestaken) == 0
    #     LLCtest = not (d[2] == 'CSULC' and LLCcomplete == False)
    #     if prereqComplete and LLCtest:
    #         pre = prereq(c)
    #         if pre > 0:
    #             # sys.stdout.write(BLUE)
    #         if d[2] == 'CSLLC':
    #             # sys.stdout.write(GREEN)
    #         print("{}) (unlocks {} courses) {} {}".format(len(choices)+1,pre,c,d[0]))
    #         # sys.stdout.write(RESET)
    #         choices.append(c)

    # if len(coursesneeded) <= 2:
    #     for c,d in coursesneeded.items():
    #         degreeplan.append([semester, c, d[0]])
    #     print("\n... and you're done!\n")
    #     break

    # new1 = int(input("\nEnter the first course to take:  "))-1
    # new2 = int(input("Enter the second course to take: "))-1
    # print()
    # # sys.stdout.write(YELLOW)
    # print("{} --> {} {}".format(semester, choices[new1], coursesneeded[choices[new1]][0]))
    # print("{} --> {} {}".format(semester, choices[new2], coursesneeded[choices[new2]][0]))
    # # sys.stdout.write(RESET)
    # degreeplan.append([semester, choices[new1], coursesneeded[choices[new1]][0]])
    # degreeplan.append([semester, choices[new2], coursesneeded[choices[new2]][0]])
    # coursestaken.update([choices[new1],choices[new2],])
    # print()

# =============== after break =================
# print degree plan summary
# print()
# for c in range(len(degreeplan)):
#     print("{:12} {:9} {}".format(degreeplan[c][0], degreeplan[c][1], degreeplan[c][2]))
#     if c % 2 == 1:
#         print()
# print("\n")


# future changes
# don't allow electives to show up until 3rd year
