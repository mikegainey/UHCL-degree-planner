###############################################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: CS1 Project
#
# Pseudocode:
#   Define a function isULC with a string parameter course
#       Set isCSCI to True if the first four characters of course is 'CSCI'
#       Set isCENG to True if the first four characters of course is 'CENG'
#       Set isULC to True if the 6th character of course is either 3 or 4
#       Return True if isCSCI or isCENG is True and isULC is True
#
#
#   Define a dictionary constant COURSECATALOG that contains information about all courses
#   pertinent to the CS BS degree, where ...
#       key   = a string representing a course ('CSCI 1471')
#       value = a tuple consisting of
#           [0] a string describing the full title of the course ('Computer Science II')
#           [1] a set of the course's prerequisites {'CSCI 1470', 'MATH 2413'}
#
#   Define a set constant LANG_PHIL_CULTURE that contains courses satisfying the
#     Language, Philosophy and Culture degree requirement
#
#   Define a set constant CREATIVE_ARTS that contains courses satisfying the
#     Creative Arts degree requirement
#
#   Define a set constant SOCIAL_SCIENCE that contains courses satisfying the
#     Social/Behavioral Science degree requirement
#
#   Define a set constant UNI_CORE that contains the University Core Requirements
#   Define a set constant MAJOR_REQ that contains the CS BS Major Requirements
#   Define a set constant LLC that contains the CS BS Lower Level Core courses
#   Set ULC to the set of courses from MAJOR_REQ that satisfy isULC
#   Define a set constant ELECTIVES to represent Major Elective courses
#
#
#   Define a function prerequisites_met that takes parameters course and coursestaken:
#       Declare that COURSECATALOG will refer to the global constant
#       Set prerequisites to the set of the course's prerequisites found in COURSECATALOG
#       Return True if prerequisites is a subset of coursestaken
#
#
#   Define a function LLCcomplete that takes a parameter coursestaken:
#       Declare that LLC will refer to the global constant
#       Return True if LLC is a subset of coursestaken
#
#
#   Define a function getChoices that takes a parameter coursestaken:
#       Declare the following global constants that will be used: LANG_PHIL_CULTURE, CREATIVE_ARTS,
#         SOCIAL_SCIENCE, UNI_CORE, MAJOR_REQ, ULC, and ELECTIVES.
#       Set choices to the union of UNI_CORE, MAJOR_REQ, LANG_PHIL_CULTURE, CREATIVE_ARTS,
#         SOCIAL_SCIENCE, and ELECTIVES.
#       Remove coursestaken from choices.
#       Remove courses with unmet prerequisites from choices.
#       If LLC is not complete:
#           remove ULC and ELECTIVES from choices.
#       If the length of the intersection of LANG_PHIL_CULTURE and coursestaken is greater than zero:
#           remove LANG_PHIL_CULTURE from choices.
#       If the length of the intersection of CREATIVE_ARTS and coursestaken is greater than zero:
#           remove CREATIVE_ARTS from choices.
#       If the length of the intersection of SOCIAL_SCIENCE and coursestaken is greater than zero:
#           remove SOCIAL_SCIENCE from choices.
#       Return choirs to the calling function/program.
#
#
#   Define a function isRubric that takes a string parameter maybeRubric:
#       If the length of maybeRubric is not 9, return False.
#       Set words to a list made from splitting maybeRubric into words
#       If the length of words is less than 2, return False.
#       Set part1 to the first word of words.
#       If part1 is either not all alphabetic or not of length 4, return False.
#       Set part2 to the second word of words.
#       If part2 is either not all decimal or not of length 4, return False.
#       Return True
#
#
#   Define a function extractRubrics that takes a parameter lines that is a list of strings
#       Set courses to an empty list.
#       Begin a loop iterating through the elements of lines using the lcv line
#           If the length of line is less than 9, skip the rest of the loop
#           Set maybeRubric to the first 9 characters of line
#           If maybeRubric returns False when passed to isRubric, skip the rest of the loop
#           Set rubric to maybeRubric
#           Append rubric to courses
#       Return courses to the calling program/function
#
#
#   Define a function add2CoursesTaken with parameters course and coursestaken:
#       Declare that COURSECATALOG will refer to the global constant
#       If course is in COURSECATALOG:
#           Add course to coursestaken
#           Print a message that course was added
#       Else, print a message saying the course is not recognized as a requirement for the CS BS degree
#
#
#   Define a function getCoursesTaken:
#       Prompt the user to enter courses (like CSCI 1470) previously completed or a file with a list of courses completed
#       Set coursestaken to the empty set.
#       Begin a loop to get user input.
#           Set course to the user's input.
#           If the user just pressed <Enter>, return coursestaken to the calling program/function.
#           If isRubric returns True with course as the argument,
#               convert course to all uppercase, and
#               pass course and coursestaken to add2CoursesTaken.
#           else,
#               Try to open a file for reading named course
#               If successful, set lines to the list of lines in the file
#               Otherwise, print a message "That's not a course or a file name"
#
#               Set courses to the return value of extractRubrics with argument lines.
#               Begin a loop iterating over courses:
#                   Call add2CoursesTaken with arguments course and coursestaken
#
#
#   define a function getTerm:
#       Set seasons to the list ["placeholder", "Fall", Spring", "Summer"]
#       Begin a loop to get user input:
#           Set season by prompting the user to enter the starting term (1=Fall, 2=Spring, and 3=Summer)
#           If season is not a decimal character,
#               print an error message, "Just the number, please" and
#               go back to the beginning of the loop.
#           Cast season to an integer
#           If season is not 1, 2, or 3,
#               print an error message, "1, 2, or 3, please" and
#               go back to the beginning of the loop.
#           Set season to the element of seasons with index season and exit the loop
#
#       Begin a loop to get user input:
#           Set year by prompting the user to enter the starting year (last 2 digits).
#           If year is not decimal or year is not of length 2,
#               Print an error message, "Just enter two digits" and
#               go back to the beginning of the loop
#           Exit the loop.
#
#       Set term to season + '20' + year
#       Return term to the calling program/function
#
#
#   Define a function incTerm with parameter currentTerm:
#       Set seasons to the list ['Fall', Spring', 'Summer']
#       Set season and year to the two words in currentTerm
#       If season is Fall,
#           Cast year to an int, add 1, and cast back to a string
#
#       Set seasonx to the index of season in seasons
#       Set nextSeasonx to (seasonx + 1) mod 3
#       Set nextSeason to the index of nextSeason in seasons
#
#       Set nextTerm to nextSeason, a space, and year
#       Return nextTerm
#
#
#   Define a function summerTerm with parameter term:
#       If term starts with 'summer' ...
#           Set summer by prompting the user "Do you want to take courses this summer?"
#           If the user just pressed <Enter>, set summer to 'no'
#           Convert summer to lowercase
#           If summer is not 'y'
#               Set term to the return value of incTerm with the argument term
#           Return term to the calling program/function
#
#
#   Define a function prereqFor with parameters course and coursestaken:
#       Declare the following global constants that will be used: COURSECATALOG, UNI_CORE, MAJOR_REQ, and ELECTIVES
#       Set coursesneeded to the union of UNI_CORE, MAJOR_REQ, and ELECTIVES, minus coursestaken
#       If the length of the intersection of LANG_PHIL_CULTURE and coursestaken is zero,
#           Add LANG_PHIL_CULTURE to coursesneeded
#       Set count to zero
#       Begin a loop iterating over coursesneeded with lcv c
#           Set prerequisites to the set of prerequisites for c
#           If the parameter course is in prerequisites, increment count
#       Return count
#
#
#   Define a function displayChoices with parameters term, choices, and coursestaken:
#       Declare the following global constants that will be used: COURSECATALOG, LANG_PHIL_CULTURE, CREATIVE_ARTS,
#         SOCIAL_SCIENCE, UNI_CORE, MAJOR_REQ, LLC, and ELECTIVES
#       Display a header for the term
#       Set courseMenu to an empty dictionary
#       Set index to 1
#
#       Set categoryChoices to a sorted list of the intersection of choices and LANG_PHIL_CULTURE
#       If the length of categoryChoices is greater than zero, display a LANG_PHIL_CULTURE heading
#       Begin a loop over categoryChoices with lcv course:
#           Display index, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove LANG_PHIL_CULTURE from choices
#
#       Set categoryChoices to a sorted list of the intersection of choices and CREATIVE_ARTS
#       If the length of categoryChoices is greater than zero, display a CREATIVE_ARTS heading
#       Begin a loop over categoryChoices with lcv course:
#           Display index, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove CREATIVE_ARTS from choices
#
#       Set categoryChoices to a sorted list of the intersection of choices and SOCIAL_SCIENCE
#       If the length of categoryChoices is greater than zero, display a SOCIAL_SCIENCE heading
#       Begin a loop over categoryChoices with lcv course:
#           Display index, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove SOCIAL_SCIENCE from choices
#
#       Set categoryChoices to a sorted list of the intersection of choices and UNI_CORE minus LLC
#       If the length of categoryChoices is greater than zero, display a University Core heading
#       Begin a loop over categoryChoices with lcv course:
#           Set isPrereqFor to the return value of prereqFor with arguments course and coursestaken
#           Display index, isPrereqFor, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove UNI_CORE from choices
#
#       Set categoryChoices to a sorted list of the intersection of choices and LLC
#       If the length of categoryChoices is greater than zero, display a CS Lower-Level Core heading
#       Begin a loop over categoryChoices with lcv course:
#           Set isPrereqFor to the return value of prereqFor with arguments course and coursestaken
#           Display index, isPrereqFor, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove LLC from choices
#
#       Set categoryChoices to a sorted list of the intersection of choices and MAJOR_REQ
#       If the length of categoryChoices is greater than zero, display a CS Major Requirements heading
#       Begin a loop over categoryChoices with lcv course:
#           Set isPrereqFor to the return value of prereqFor with arguments course and coursestaken
#           Display index, isPrereqFor, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove MAJOR_REQ from choices
#       
#       Set categoryChoices to a sorted list of the intersection of choices and ELECTIVES
#       If the length of categoryChoices is greater than zero, display a CS Major Electives heading
#       Begin a loop over categoryChoices with lcv course:
#           Display index, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove ELECTIVES from choices
#
#       Return courseMenu to the calling program/function
#
#
#   Define a function chooseCourses with parameters term, courseMenu, degreeplan, and coursestaken:
#       Declare that COURSECATALOG will refer to the global constant
#       Set termSummary to the empty list
#       Begin a loop to get user input:
#           Set choice from a user prompt to select a course by number, pressing <Enter> when finished
#           If the user just presses <Enter>, exit the loop
#           If choice is not a decimal character,
#               print an error message and go to the beginning of the loop
#           Cast choice to an integer
#           If choice is not in courseMenu,
#               display an error message and go to the beginning of the loop
#           Set course to courseMenu with index choice
#           Add course to coursestaken
#           Set entry to a tuple consisting of term, course, and the name of the course
#           Append entry to degreeplan
#           Append to termSummary: the term, course, and course name
#
#       Begin a loop of termSummary with lcv c
#           Display c
#       Append to degreeplan a tuple with three blanks to signal a blank line
#       Return degreeplan to the calling program/function
#
#
#   Define a function printSummary with parameter degreeplan:
#       Display a heading: "Your degree plan summary"
#
#       Begin a loop of degreeplan with lcv c:
#           Display all three elements of c
#
#
#   Define a function saveSummary with parameter degreeplan:
#       Prompt the user to save the degree plan summary to a file
#       Set filename to the user's input
#       If the user just pressed <Enter>, return to the calling program/function
#       Try to open filename for writing
#           Write a heading, "Your degree plan summary"
#           Begin a loop over degreeplan with lcv c:
#               Write all three elements of c
#           Display a message, filename "contains your degree plan summary"
#       If unsuccessful, print a message, "couldn't write to the file"
#
#
#   Define a function main:
#       Set degreeplan to the empty list
#       Set coursestaken to the return value of getCoursesTaken
#       Set term to the return value of getTerm
#       Begin a loop:
#           Set choices to the return value of getChoices with argument coursestaken
#           If the length of choices is zero, exit the loop
#           Set term to the return value of summerTerm with argument term
#           Set courseMenu to the return value of displayChoices with arguments term, choices, and coursestaken
#           Set degreeplan to the return value of chooseCourses with arguments term, courseMenu, degreeplan, and coursestaken
#           Set term to the return value of incTerm with argument term
#       Call the printSummary function with argument degreeplan
#       Call the saveSummary function with argument degreeplan
#
#
#   If the name of the running module is '__main__' then call the main function
#
#
###############################################################################

# UNDERGRADUATE Catalog 2017-2018, Computer Science B.S.
# Degree Requirements: https://catalog.uhcl.edu/current/undergraduate/degrees-and-programs/bachelors/computer-science-bs

# The 2-page Computer Science degreeplan can be found at:
# https://www.uhcl.edu/academics/degrees/documents/cse/wbs-computerscience.pdf


####################
# Global Constants #
####################


# COURSECATALOG is a dictionary where
#   key:   is a string representing a course number, like 'PHYS 2325'
#   value: is a tuple consisting of
#     - a string describing the full title of the course, "University Physics I"
#     - a set of prerequisites : str, {"MATH 2413", "MATH 2414"}

# verified against the UHCL Undergraduate Catalog 2017-2018 on (date)
COURSECATALOG = {
    # Communication (6 hours)
    "WRIT 1301": ("Composition I", set()),
    "WRIT 1302": ("Composition II", {"WRIT 1301"}),

    # Mathematics (4 hours), # this has a prerequisite, but it's not part of the degree requirements
    "MATH 2413": ("Calculus I", set()),

    # Life and Physical Sciences (6 hours)
    "PHYS 2325": ("University Physics I and Lab (PHYS 2125)", {"MATH 2413"}),
    "PHYS 2326": ("University Physics II and Lab (PHYS 2126)", {"MATH 2414", "PHYS 2325"}),

    # Language, Philosophy and Culture (3 hours)
    "HUMN 1301": ("Humanities", set()),
    "LITR 2341": ("Literature and Experience", {"WRIT 1301"}),
    "PHIL 1301": ("Introduction to Philosophy", set()),
    "WGST 1301": ("Gender Matters: Introduction to Women's and Gender Studies", set()),

    # Creative Arts (3 Hours)
    "ARTS 1303": ("World Art Survey I", set()),
    "ARTS 1304": ("World Art Survey II", set()),
    "ARTS 2379": ("Arts and the Child", set()),

    # American History (6 hours)
    "HIST 1301": ("United States History I", set()),
    "HIST 1302": ("United States History II", set()),

    # Government/Political Science (6 hours)
    "POLS 2305": ("Federal Government", set()),
    "POLS 2306": ("Texas Government", set()),

    # Social and Behavioral Sciences (3 hours)
    "ANTH 2346": ("General Anthropology", set()),
    "CRIM 1301": ("Introduction to Criminal Justice", set()),
    "ECON 2301": ("Principles of Macroeconomics", set()),
    "ECON 2302": ("Principles of Microeconomics", set()),
    "GEOG 1303": ("World Regional Geography", set()),
    "PSYC 2301": ("Introduction to Psychology", set()),
    "SOCI 1301": ("Introduction to Sociology", set()),

    # Component Area Option (6 hours)
    "COMM 1315": ("Public Speaking", set()),
    "PSYC 1100": ("Learning Frameworks", set()),

    # Major Requirements (67 hours)
    "CHEM 1311": ("General Chemistry I and Lab (CHEM 1111)", set()),
    "MATH 2305": ("Discrete Mathematics", {"MATH 2413"}),
    "MATH 2318": ("Linear Algebra", {"MATH 2413"}),
    "MATH 2414": ("Calculus II", {"MATH 2413"}),
    "MATH 2320": ("Differential Equations", {"MATH 2414"}),
    "STAT 3334": ("Probability & Statistics for Scientists & Engineers", {"MATH 2413", "MATH 2414"}),
    "CSCI 1470": ("Computer Science I", set()),
    "CSCI 1471": ("Computer Science II", {"CSCI 1470"}), # MATH 2413 was a prereq in the 2016-17 catalog
    "CSCI 3331": ("Computer Organization & Assembly Language", {"CSCI 2315", "MATH 2305", "MATH 2414",
                                                                "PHYS 2325",  "PHYS 2326"}),
    "CSCI 2315": ("Data Structures", {"CSCI 1471"}),
    "CSCI 3352": ("Advanced Data Structures", {"CSCI 2315", "MATH 2305", "MATH 2414", "PHYS 2325", "PHYS 2326"}),
    "CSCI 4333": ("Design of Database Systems", {"CSCI 2315"}),
    "CSCI 3321": ("Numerical Methods", {"MATH 2318", "MATH 2320", "CSCI 1471"}),
    "CSCI 4354": ("Operating Systems                       (take with CENG 3351)",
                  {"CSCI 2315", "CSCI 3331", "MATH 2305", "MATH 2414", "PHYS 2325", "PHYS 2326"}),

    "CENG 3312": ("Digital Circuits & Lab (CENG 3112)", {"MATH 2414", "PHYS 2326"}),
    "CENG 3331": ("Intro to Telecommunications and Networks & Lab (CENG 3131)",  {"CENG 3312"}),
    "CENG 3351": ("Computer Architecture & Lab (CENG 3151) (take with CSCI 4354)", {"CENG 3331"}), # prereq changed from 2016-17

    "SWEN 4342": ("Software Engineering", {"CSCI 1470", "CSCI 2315"}), # CSCI 1470 prereq implied; CSCI 2315 recommended
    "WRIT 3315": ("Technical Writing", {"WRIT 1301", "WRIT 1302"}),
    "CSCI 4388": ("Senior Project in Computer Science", {"CSCI 3352", "SWEN 4342"}),

    # CSCI/CINF Major Electives; taken junior or senior year
    "CSCI 33x1": ("CSCI/CINF 33xx or 43xx upper level elective", set()),
    "CSCI 33x2": ("CSCI/CINF 33xx or 43xx upper level elective", set()),
    "CSCI 33x3": ("CSCI/CINF 33xx or 43xx upper level elective", set()),
    "CSCI 32xx": ("CSCI/CINF 32xx or 42xx upper level elective", set())
}

# Language, Philosophy and Culture (3 hours required)
LANG_PHIL_CULTURE = {"HUMN 1301", "LITR 2341", "PHIL 1301", "WGST 1301"}

# Creative Arts (3 hours required)
CREATIVE_ARTS = {"ARTS 1303", "ARTS 1304", "ARTS 2379"}

# Social and Behavioral Sciences (3 hours required)
SOCIAL_SCIENCE = {"ANTH 2346", "CRIM 1301", "ECON 2301", "ECON 2302", "GEOG 1303", "PSYC 2301", "SOCI 1301"}

# University Core
UNI_CORE = {'WRIT 1301', 'WRIT 1302', 'MATH 2413', 'PHYS 2325', 'PHYS 2326', 'HIST 1301', 'HIST 1302',
           'POLS 2305', 'POLS 2306', 'COMM 1315', 'PSYC 1100'}

# Major Requirements
MAJOR_REQ = {'CHEM 1311', 'MATH 2305', 'MATH 2318', 'MATH 2414', 'MATH 2320', 'STAT 3334',
            'CSCI 1470', 'CSCI 1471', 'CSCI 3331', 'CSCI 2315', 'CSCI 3352', 'CSCI 4333', 'CSCI 3321',
            'CSCI 4354', 'CENG 3312', 'CENG 3331', 'CENG 3351', 'SWEN 4342', 'WRIT 3315', 'CSCI 4388'}

# CS Lower-Level Core; note there is some overlap with UNI_CORE
LLC = {'CSCI 1470', 'CSCI 1471', 'CSCI 2315', 'PHYS 2325', 'PHYS 2326', 'MATH 2413', 'MATH 2414', 'MATH 2305', 'WRIT 1301'}

# needed for hours computation and classification determination
HASLAB = {'PHYS 2325', 'PHYS 2326', 'CHEM 1311', 'CENG 3312', 'CENG 3331', 'CENG 3351'}

# this function definition needs to come before the ULC definition below
def isULC(course):
    '''Given a course, return True if the course is an upper-level CSCI or CENG course.
       isULC(course : str) -> bool
       Used to build the set constant ULC.
    '''
    isCSCI = course[:4] == 'CSCI'   # CSCI course?
    isCENG = course[:4] == 'CENG'   # CENG course?
    isULC = course[5] in ['3', '4'] # 3000 or 4000 level course?
    return (isCSCI or isCENG) and isULC

# CS Upper-Level Core; after this constant is built, it doesn't change
ULC = {course for course in MAJOR_REQ if isULC(course)}


# Major electives; modified the last digit because rubrics must be unique
ELECTIVES = {"CSCI 33x1", "CSCI 33x2", "CSCI 33x3", "CSCI 32xx"}


########################
# Function Definitions #
########################


def prerequisites_met(course, coursestaken):
    '''Given a course and courses taken, return True if the course's prerequisites have been met.
       prerequisites_met(course : str, coursestaken : set) -> bool
    '''
    global COURSECATALOG

    # get the set of prerequisites for the course
    prerequisites = COURSECATALOG[course][1] 

    # return True if every element of prerequisites is in coursestaken
    return prerequisites.issubset(coursestaken) 


def LLCcomplete(coursestaken):
    '''Given the set of courses taken, return True if the CS LLC is complete.
       LLCcomplete(coursestaken : set) -> bool
    '''
    global LLC

    # return True if every element of LLC issubset of coursestaken
    return LLC.issubset(coursestaken) 


def getChoices(coursestaken):
    '''Given the set of courses taken, return the set of courses eligible to be taken (choices)
       getChoices(coursestaken : set) -> set
    '''
    global LANG_PHIL_CULTURE
    global CREATIVE_ARTS
    global SOCIAL_SCIENCE
    global UNI_CORE
    global MAJOR_REQ
    global ULC
    global ELECTIVES

    # at the end of this function, choices will be the list of courses eligible to be taken
    choices = UNI_CORE | MAJOR_REQ | LANG_PHIL_CULTURE | CREATIVE_ARTS | SOCIAL_SCIENCE | ELECTIVES

    # remove coursestaken from choices
    choices -= coursestaken

    # remove courses where prerequisites have not been met
    choices = {course for course in choices if prerequisites_met(course, coursestaken)}

    # remove ULC and ELECTIVES if LLC not complete
    if not LLCcomplete(coursestaken):
        choices -= ULC | ELECTIVES # remove ULC and ELECTIVES

    # if LANG_PHIL_CULTURE requirement met (1 course), remove all LANG_PHIL_CULTURE courses from choices
    if len(LANG_PHIL_CULTURE & coursestaken) > 0: # if a LANG_PHIL_CULTURE course has already been taken
        choices -= LANG_PHIL_CULTURE              # remove all LANG_PHIL_CULTURE courses from the choices list

    # if CREATIVE_ARTS requirement met (1 course), remove all CREATIVE_ARTS courses from choices
    if len(CREATIVE_ARTS & coursestaken) > 0: # if the intersection of CREATIVE_ARTS and coursestaken is greater than zero
        choices -= CREATIVE_ARTS              # remove all CREATIVE_ARTS courses from the choices list

    # if SOCIAL_SCIENCE requirement met (1 course), remove all SOCIAL_SCIENCE courses from choices
    if len(SOCIAL_SCIENCE & coursestaken) > 0: # if the intersection of SOCIAL_SCIENCE and coursestaken is greater than zero
        choices -= SOCIAL_SCIENCE              # remove all SOCIAL_SCIENCE courses from the choices list

    return choices


def isRubric(maybeRubric):
    '''Given a string, return True if the string consists of 4 alpha + ' ' + 4 decimal characters
       isRubric(maybeRubric : str) -> bool
       the alpha characters can be uppercase or lowercase
    '''
    # course numbers are always 9 characters (like 'CSCI 1470')
    if len(maybeRubric) != 9: 
        return False

    words = maybeRubric.split()

    # make sure the line has at least 2 words: CSCI 1470 Computer Science ...
    if len(words) != 2:
        return False

    # first word should be 4 alphabetic characters: CSCI
    part1 = words[0]
    if not (part1.isalpha() and len(part1) == 4): 
        return False

    # second word should be 4 decimal characters: 1470
    part2 = words[1]
    if not (part2.isdecimal() and len(part2) == 4): 
        return False

    return True # return True if above conditions are met


def extractRubrics(lines):
    '''Given a list of lines from a file, return an ordered list of valid course numbers.
       extractRubrics(lines : [str]) -> [str]
       These course numbers might not apply to the CS BS degree (checked in add2CoursesTaken)
    '''
    courses = list()
    for line in lines:

        if len(line) < 9:             # the line is too short to contain a course number
            continue

        maybeRubric = line[:9]        # the part of the line to check

        if not isRubric(maybeRubric): # if not a course number, loop back
            continue

        rubric = maybeRubric          # at this point, it's a confirmed course number (format)
        rubric = rubric.upper()       # the course number must be uppercase (used as a key in COURSECATALOG : dict)

        courses.append(rubric)        # add the course number to the output list

    return courses


def add2CoursesTaken(course, coursestaken):
    '''Add a course to coursestaken only if it applies to the CS BS degree
       add2CoursesTaken(course : str, coursestaken : set) -> NoneType (+ mutating coursestaken)
       used twice in getCoursesTaken (so this function prevents code duplication)
    '''
    global COURSECATALOG

    if course in COURSECATALOG:

        coursestaken.add(course)
        print("added {} {}".format(course, COURSECATALOG[course][0]))

    else:
        print("----- {} not recognized as a requirement for the Computer Science B.S. degree".format(course))


def getCoursesTaken():
    '''Prompt the user to enter courses previously completed and/or load courses from file(s).
       getCoursesTaken() -> NoneType (+ calling add2CoursesTaken mutator function)'''

    print("\nEnter course numbers (like CSCI 1470) that you have previously completed and/or the names of files containing course numbers.\n")

    coursestaken = set()

    while True:
        course = input("Enter a course number or a file name. Press <Enter> when finished: ")

        # the sentinel
        if course == '':
            return coursestaken

        # the input string is a course number
        if isRubric(course):
            course = course.upper()

            # add to coursestaken only if the course applies to the CS BS degree
            add2CoursesTaken(course, coursestaken)

        # the input string is not a course number; see if it's a file name
        else:
            try:
                with open(course, 'r') as file:
                    lines = list(file) # a list of lines in the file
            except:
                print("----- That's not a course number or a file name.\n")
                continue

            # valid filename; lines is populated; get the set of courses
            courses = extractRubrics(lines)
            print()

            # add the list of courses to coursestaken if it applies to the CS BS degree
            for course in courses:
                add2CoursesTaken(course, coursestaken)

        print()


def getTerm():
    '''Prompt the user to enter the starting term (like Fall 2017)
       getTerm() -> str
    '''
    seasons = ["placeholder", "Fall", "Spring", "Summer"]

    while True:
        # print("\nEnter your starting term: 1=Fall, 2=Spring, 3=Summer")
        season = input("\nEnter your starting term (1=Fall, 2=Spring, 3=Summer): ")

        if not season.isdecimal(): # season has non-decimal characters
            print("----- Just the number, please.")
            continue

        season = int(season)
        if season not in [1, 2, 3]: # season is out of range
            print("----- 1, 2, or 3, please.")
            continue

        # season has been validated
        season = seasons[season] # season = Fall, Spring, or Summer
        break

    while True:
        year = input("Enter your starting year (last 2 digits only): ")

        if not (year.isdecimal() and len(year) == 2):
            print("----- Just 2 digits, please.")
            continue

        # year has been validated
        break

    term = season + " 20" + year

    print()
    return term


def incTerm(currentTerm):
    '''Given a current term, return the next term
       incTerm(currentTerm : str) -> str
       This function will produce a runtime error
         if term's fist word is not in seasons (but that should never happen).
    '''
    seasons = ["Fall", "Spring", "Summer"]

    season, year = currentTerm.split()

    if season == 'Fall':
        year = int(year) + 1
        year = str(year)

    seasonx = seasons.index(season)
    nextSeasonx = (seasonx + 1) % 3
    nextSeason = seasons[nextSeasonx]

    nextTerm = nextSeason + ' ' + year

    return nextTerm


def summerTerm(term):
    '''If current term is summer, ask if user wants to take summer courses; return next term
       summerTerm(term : str) -> str
       (default = no)
    '''
    if term.startswith('Summer'):
        summer = input("Do you want to take courses in the summer of {}? (y/N) ".format(term[-4:]))
        print()
        summer = summer or 'n'
        summer = summer[0].lower()
        if summer != 'y':
            term = incTerm(term)

    return term


def prereqFor(course, coursestaken):
    '''Given a course, return the number of (still needed) courses for which that course is a prerequisite
      prereqFor(course : str, coursestaken : set) -> int
    '''
    global COURSECATALOG
    global UNI_CORE
    global MAJOR_REQ

    coursesneeded = UNI_CORE | MAJOR_REQ
    
    # because WRIT 1301 is a prerequisite for LITR 2341 (in LANG_PHIL_CULTURE)
    if len(LANG_PHIL_CULTURE & coursestaken) == 0: # if the lang/phil/culture requirement is not complete
        coursesneeded |= LANG_PHIL_CULTURE         # add it to courses needed

    # CREATIVE_ARTS and SOCIAL_SCIENCE don't have to be here because those courses don't have prerequisites
    # Although electives may have prerequisites, my program doesn't have the catalog information to process them here

    count = 0
    for c in coursesneeded:
        prerequisites = COURSECATALOG[c][1]
        if course in prerequisites:
            count += 1

    return count


def classification(coursestaken):
    '''Given coursestaken, return a tuple with (classification, total hours completed) where classification is ...
       freshman for 1-29 hours, sophomore for 30-59 hours, junior for 60-89 hours, and senior for 90+ hours
       classificaiton(coursestaken : set) -> (str, int)
    '''
    totalHours = 0
    for course in coursestaken:
        totalHours += int(course[-3]) # "CSCI 1470"[3] = 4

    # add another hour for each course with a lab
    labs = coursestaken & HASLAB # coursestaken that have labs
    numlabs = len(labs) # the number of labs taken
    totalHours += numlabs

    # determine classification from totalHours
    if totalHours <= 29:
        standing = 'freshman'
    elif 30 <= totalHours <= 59:
        standing = 'sophomore'
    elif 60 <= totalHours <= 89:
        standing = 'junior'
    else:
        standing = 'senior'

    return (standing, totalHours)


def displayChoices(term, choices, coursestaken):
    '''Given a set of course choices, display and return a choice dictionary (menu)
       displayChoices(term : str, choices : set, coursestaken : set) -> {index: course}
    '''
    global COURSECATALOG
    global LANG_PHIL_CULTURE
    global CREATIVE_ARTS
    global SOCIAL_SCIENCE
    global UNI_CORE
    global MAJOR_REQ
    global LLC
    global ELECTIVES

    # standing = (classification, totalHours) where classification = freshman | sophomore | ...
    standing = classification(coursestaken)
    
    print('=' * 80)
    left = "{} choices:".format(term)
    right = "({} with {} hours)".format(standing[0], standing[1])
    print("{:<30}{:>50}".format(left, right))
    print('=' * 80)

    courseMenu = {} # a dictionary with key = menu number, value = course number
    index = 1       # the menu numbers

    # display Language, Philosophy, Culture courses
    categoryChoices = sorted(list(choices & LANG_PHIL_CULTURE))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nLanguage, Philosophy, and Culture (3 hours, choose one course)")

    for course in categoryChoices:
        print("{:4}) {} {}".format(index, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    choices -= LANG_PHIL_CULTURE

    # display Creative Arts courses
    categoryChoices = sorted(list(choices & CREATIVE_ARTS))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nCreative Arts (3 hours, choose one course)")

    for course in categoryChoices:
        print("{:4}) {} {}".format(index, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    choices -= CREATIVE_ARTS

    # display Social Science courses
    categoryChoices = sorted(list(choices & SOCIAL_SCIENCE))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nSocial/Behavioral Science (3 hours, choose one course)")

    for course in categoryChoices:
        print("{:4}) {} {}".format(index, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    choices -= SOCIAL_SCIENCE

    # display UCore UNI_CORE choices (LLC in UNI_CORE is listed in CS LLC)
    categoryChoices = sorted(list(choices & UNI_CORE - LLC))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nOther University Core Requirements")

    for course in categoryChoices:
        isPrereqFor = prereqFor(course, coursestaken)
        print("{:4}) (prereq for {} courses) {} {}".format(index, isPrereqFor, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    choices -= UNI_CORE - LLC # check this for correctness! I think it's right.

    # display CS LLC choices
    categoryChoices = sorted(list(choices & LLC))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nComputer Science Lower-Level Core (LLC)")

    for course in categoryChoices:
        isPrereqFor = prereqFor(course, coursestaken)
        print("{:4}) (prereq for {} courses) {} {}".format(index, isPrereqFor, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    choices -= LLC

    # display CS other major requirements choices
    categoryChoices = sorted(list(choices & MAJOR_REQ))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nOther Computer Science Major Requirements")

    for course in categoryChoices:
        isPrereqFor = prereqFor(course, coursestaken)
        print("{:4}) (prereq for {} courses) {} {}".format(index, isPrereqFor, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    choices -= MAJOR_REQ

    # display CS electives
    categoryChoices = sorted(list(choices & ELECTIVES))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nComputer Science Major Electives (taken junior or senior year)")

    for course in categoryChoices:
        # assuming CS electives aren't going to be prerequisites for anything else
        print("{:4}) {} {}".format(index, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    choices -= ELECTIVES

    return courseMenu


def chooseCourses(term, courseMenu, degreeplan, coursestaken):
    '''Let the user choose courses to take for the listed term; update coursestaken
       chooseCourses(courseMenu : dict, coursestaken : set) -> coursesChosen : [course: str]
       ... and coursestaken is also updated
    '''
    global COURSECATALOG

    print()
    termSummary = [] # a list of courses chosen for that term only

    while True: # the loop to collect chosen courses

        choice = input("Select a course by number.  Press <Enter> when finished: ")
        if choice == '':
            break

        # check for non-decimal characters
        if not choice.isdecimal():
            print("----- Enter the number only.")
            continue

        # verify the choice is in the courseMenu
        choice = int(choice)
        if choice not in courseMenu:
            print("----- Invalid entry.")
            continue

        course = courseMenu[choice]
        coursestaken.add(course) # this mutates coursestaken globally!

        entry = (term, course, COURSECATALOG[course][0])
        degreeplan.append(entry)

        termSummary.append("{} --> {} {}".format(term, course, COURSECATALOG[course][0]))

    # only print a term summary if there is something to print
    if len(termSummary) > 0:
        print()
        for c in termSummary:
            print(c)

        degreeplan.append(('', '', '')) # a separator between terms to make output formatting easier
            
    return degreeplan


def printSummary(degreeplan):
    '''Print the degree plan summary, the final output
       printSummary(degreeplan : [(str, str, str)]) -> NoneType (+ desired side effects)
    '''
    print('=' * 80)
    print("Your degree plan summary:")
    print('=' * 80)
    print()

    for c in degreeplan:
        # c[0] = term, c[1] = course number, c[2] = course title
        print("{:12} {:9} {}".format(c[0], c[1], c[2]))

    print('=' * 80)
    print()


def saveSummary(degreeplan):
    '''Save the degree plan summary to a file
       saveSummary(degreeplan : [(str, str, str)]) -> NoneType (+ desired side effects)
    '''
    # ask user if he/she wants to save degreeplan summary to a file
    print("If you want to save this summary to a file, ", end="")
    filename = input("enter a filename, otherwise just press <Enter> to quit: ")

    # just return if user presses <Enter>
    if filename == '':
        return

    # a file name was given; write to the file
    try:
        with open(filename, 'w') as file:
            file.write("{}{}".format('=' * 80, '\n'))
            file.write("Your degree plan summary:\n")
            file.write("{}{}".format('=' * 80, '\n'))
            file.write('\n')

            for c in degreeplan:
                # c[0] = term, c[1] = course number, c[2] = course title
                file.write("{:12} {:9} {}\n".format(c[0], c[1], c[2]))
            file.write("{}{}".format('=' * 80, '\n'))

        print("{} contains your degree plan summary!\n".format(filename))

    except:
        print("Couldn't write to the file!")
    # return without doing anything


def main():

    # print a welcome message
    # print("blah, blah, blah, ...")
    
    # this will eventually hold the completed degree plan
    degreeplan = []

    # let the user enter courses previously taken
    coursestaken = getCoursesTaken()

    # let the user enter the starting term (like Fall 2017)
    term = getTerm()

    while True:

        # a set of courses eligible to be taken
        choices = getChoices(coursestaken)

        # are all courses completed? If so, print the final degree plan summary
        if len(choices) == 0:
            break

        # if term is summer, ask if user wants to take classes in the summer; if not, do incTerm
        term = summerTerm(term)

        # display a menu of course choices for the term
        courseMenu = displayChoices(term, choices, coursestaken)

        # choose courses for the term; update degreeplan; mutates coursestaken!
        degreeplan = chooseCourses(term, courseMenu, degreeplan, coursestaken)

        term = incTerm(term)

        print()

    # prints degree plan summary to the screen
    printSummary(degreeplan)

    # saves degree plan summary to a file if the user gives a file name
    saveSummary(degreeplan)

    # THE END


# this allows this program to be imported (without executing) into a unittest script for testing
if __name__ == "__main__":
    main()


# TODO:
# - print a nice intro and explanatory text here and there
# - see if a global coursesneeded variable is practical; certainly would be more efficient

#   Don't show courses as choices until they have the proper standing when applicable.
#   - electives (junior or senior); CSCI 4354 (senior)

# - replace the term "rubric" with "course number" because I'm not using that term correctly.
#   I think "CSCI" is a rubric.  "CSCI 1470" will be called a "course number."

# - check and correct all course numbers in constants; they must be uppercase to correctly match keys in COURSECATALOG
# - remove all un-needed global statements (most or all of them); only needed if the global will be mutated (right?)

# Functions:
# good tested isULC(course)
# good tested prerequisites_met(course, coursestaken)
# good tested LLCcomplete(coursestaken)
# good tested getChoices(coursestaken)
# good tested isRubric(rubric)
# good tested extractRubrics(lines)
# good tested add2CoursesTaken(course, coursestaken)
# good tested getCoursesTaken()
# good tested getTerm()
# good tested incTerm(term)
# good tested summerTerm(term)
# good tested prereqFor(course, coursestaken)
#             classificaiton(coursetaken)
# good tested displayChoices(term, choices, coursestaken)
# good tested chooseCourses(term, courseMenu, degreeplan, coursestaken)
# good tested printSummary(degreeplan)
# good tested saveSummary(degreeplan, filename)
# good tested main()
