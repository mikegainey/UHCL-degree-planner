# Need help figuring out what courses to take and in what order?  Then, run this program!

# Undergraduate Catalog 2017-2018, Computer Science B.S.
# Degree Requirements: https://catalog.uhcl.edu/current/undergraduate/degrees-and-programs/bachelors/computer-science-bs

# The 2-page Computer Science degreeplan can be found at:
# https://www.uhcl.edu/academics/degrees/documents/cse/wbs-computerscience.pdf


# This function has to be defined first in order for the constant ULC to be defined.
# That's why it's not with the other function definitions.
def isULC(course):
    '''Given a course, return True if the course is an upper-level CSCI or CENG course.
       isULC(course : str) -> bool
       Used to build the set constant ULC
    '''
    isCSCI = course[:4] == 'CSCI'   # CSCI course?
    isCENG = course[:4] == 'CENG'   # CENG course?
    isULC = course[5] in ['3', '4'] # 3000 or 4000 level course?
    return (isCSCI or isCENG) and isULC


####################
# Global Constants #
####################


# COURSECATALOG is a dictionary where
#   key:   is a string representing a course rubric, like 'PHYS 2325'
#   value: is a tuple consisting of
#     - a string describing the full title of the course, "University Physics I"
#     - a set of prerequisites : str, {"MATH 2413", "MATH 2414"}

COURSECATALOG = {
    # Communication (6 hours)
    "WRIT 1301": ("Composition I", set()),
    "WRIT 1302": ("Composition II", {"WRIT 1301"}),

    # Mathematics (3 hours)
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
    "HIST 1301": ("U.S. History I", set()),
    "HIST 1302": ("U.S. History II", set()),

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
    "MATH 2305": ("Discrete Math", {"MATH 2413"}),
    "MATH 2318": ("Linear Algebra", {"MATH 2413"}),
    "MATH 2414": ("Calculus II", {"MATH 2413"}),
    "MATH 2320": ("Differential Equations", {"MATH 2414"}),
    "STAT 3334": ("Probability & Statistics ...", {"MATH 2413", "MATH 2414"}),
    "CSCI 1470": ("Computer Science I", set()),
    "CSCI 1471": ("Computer Science II", {"CSCI 1470", "MATH 2413"}),
    "CSCI 3331": ("Computer Organization & Assembly Language", {"CSCI 2315", "MATH 2305", "MATH 2414",
                                                                "PHYS 2325",  "PHYS 2326"}),
    "CSCI 2315": ("Data Structures", {"CSCI 1471"}),
    "CSCI 3352": ("Advanced Data Structures", {"CSCI 2315", "MATH 2305", "MATH 2414", "PHYS 2325", "PHYS 2326"}),
    "CSCI 4333": ("Design of Database Systems", {"CSCI 2315"}),
    "CSCI 3321": ("Numerical Methods", {"MATH 2318", "MATH 2320", "CSCI 1471"}),
    "CSCI 4354": ("Operating Systems                       (take with CENG 3351)",
                  {"CSCI 2315", "CSCI 3331", "MATH 2305", "MATH 2414", "PHYS 2325", "PHYS 2326"}),

    "CENG 3312": ("Digital Circuits & Lab (CENG 3112)", {"MATH 2414", "PHYS 2326"}),
    "CENG 3331": ("Intro to Telecom and Neworks & Lab (CENG 3131)",  {"CENG 3312"}),
    "CENG 3351": ("Computer Architecture & Lab (CENG 3151) (take with CSCI 4354)", {"CENG 3312"}),

    "SWEN 4342": ("Software Engineering", {"CSCI 1470", "CSCI 2315"}),
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

# CS lower-level core; there is some overlap with UNI_CORE
LLC = {'CSCI 1470', 'CSCI 1471', 'CSCI 2315', 'PHYS 2325', 'PHYS 2326', 'MATH 2413', 'MATH 2414', 'MATH 2305', 'WRIT 1301'}

# CS upper-level core; after this constant is built, it doesn't change
ULC = {c for c in MAJOR_REQ if isULC(c)}

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

    prerequisites = COURSECATALOG[course][1] # get the set of prerequisites for the course

    return prerequisites.issubset(coursestaken) # True if every element of prerequisities is in coursestaken


def LLCcomplete(coursestaken):
    '''Given the set of courses taken, return True if the CS LLC is complete.
       LLCcomplete(coursestaken : set) -> bool
    '''
    global LLC

    return LLC.issubset(coursestaken) # True if every element of LLC issubset of coursestaken


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

    # remove courses where prerequisitives have not been met
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
    if len(maybeRubric) != 9: # rubrics are always 9 characters (like 'CSCI 1470')
        return False

    words = maybeRubric.split()

    if len(words) < 2: # make sure the line has at least 2 words: CSCI 1470 Computer Science ...
        return False

    part1 = words[0]
    if not (part1.isalpha() and len(part1) == 4): # should be 4 alphabetic characters: CSCI
        return False

    part2 = words[1]
    if not (part2.isdecimal() and len(part2) == 4): # should be 4 decimal characters: 1470
        return False

    return True


def extractRubrics(lines):
    '''Given a list of lines from a file, return a set of valid rubrics.
       extractRubrics(lines : [str]) -> {str}
    '''
    courses = set()
    for line in lines:

        if len(line) < 9: # the line is too short to contain a rubric
            continue

        maybeRubric = line[:9] # the part of the line to check

        if not isRubric(maybeRubric): # if not a rubric, loop back
            continue

        rubric = maybeRubric # at this point, it's a confirmed rubric (format)

        if rubric in COURSECATALOG:
            courses.add(rubric)
            print("added {} {}".format(rubric, COURSECATALOG[rubric][0]))

        else:
            print("----- {} not recognized as a requirement for the Computer Science B.S. degree".format(rubric))

    return courses


def getCoursesTaken():
    '''Prompt the user to enter courses previously completed.
       getCoursesTaken() -> set'''

    print("\nEnter courses by rubric (like CSCI 1470) that you have previously completed and/or names of files containing course rubrics.\nPress <Enter> when finished.\n")

    coursestaken = set()

    while True:
        course = input("  Enter a course rubric or a file name: ")

        # the sentinel
        if course == '':
            return coursestaken

        # if not a valid rubric, treat as a file name
        if not isRubric(course): # course doesn't fit the rubric pattern
            try:                 # check for a file name
                with open(course, 'r') as file:
                    lines = list(file) # a list of lines in the file
            except:
                print("--That's not a rubric or a file name.\n")
                continue

            # valid filename; lines is populated; make a list of courses
            print()
            courses = extractRubrics(lines)
            print()

            # add the list of courses to coursestaken
            coursestaken |= courses
            continue # don't add the filename to the set of rubrics!

        else: # isRubric(course) == True

            course = course.upper()
            if course in COURSECATALOG:

                coursestaken.add(course)
                print("added {} {}".format(course, COURSECATALOG[course][0]))

            else:
                print("----- {} not recognized as a requirement for the Computer Science B.S. degree".format(course))

            print()


def getTerm():
    '''Prompt the user to enter the starting term (like Fall 2017)
       getTerm() -> str
    '''
    seasons = ["placeholder", "Fall", "Spring", "Summer"]

    print("\nEnter your starting term: 1=Fall, 2=Spring, 3=Summer")
    season = int(input("\n  Enter 1, 2, or 3: ")) # check the input first
    season = seasons[season]

    year = input("\n  Enter your starting 2-digit year: ") # check the input

    term = season + " 20" + year
    print()
    return term


def incTerm(term):
    '''Given a term, return the next term
       incTerm(term : str) -> str
    '''
    seasons = ["Fall", "Spring", "Summer"]

    season, year = term.split()

    if season == 'Fall':
        year = int(year) + 1
        year = str(year)

    seasonx = seasons.index(season) # this will fail easily
    nextseasonx = (seasonx + 1) % 3
    nextseason = seasons[nextseasonx]

    nextterm = nextseason + ' ' + year

    return nextterm


def prereqFor(course, coursestaken):
    '''Given (the parameters), return the number of needed courses for which that course is a prerequisite
      prereqFor(course : str, coursestaken : set) -> int
    '''
    global COURSECATALOG
    global UNI_CORE
    global MAJOR_REQ
    global ELECTIVES

    coursesneeded = UNI_CORE | MAJOR_REQ | ELECTIVES - coursestaken

    # because WRIT 1301 is a prerequisite for LITR 2341 (in LANG_PHIL_CULTURE)
    if len(LANG_PHIL_CULTURE & coursestaken) == 0: # if the lang/phil/culture requirement is not complete
        coursesneeded |= LANG_PHIL_CULTURE         # add it to courses needed

    # CREATIVE_ARTS and SOCIAL_SCIENCE don't have to be here because thoses courses don't have prerequisites

    count = 0
    for c in coursesneeded:
        prerequisites = COURSECATALOG[c][1]
        if course in prerequisites:
            count += 1

    return count


def displayChoices(term, choices, coursestaken):
    '''Given a set of course choices, display and return a choice dictionary (menu)
       displayChoices(term : str, choices : set, coursetaken : set) -> {index: course}
    '''
    global COURSECATALOG
    global LANG_PHIL_CULTURE
    global CREATIVE_ARTS
    global SOCIAL_SCIENCE
    global UNI_CORE
    global MAJOR_REQ
    global LLC
    global ELECTIVES

    print("{}\n{} choices:\n{}".format('=' * 80, term, '=' * 80))

    courseMenu = {} # a dictionary with key = choice number, value = course rubric
    index = 1

    choices2 = choices.copy()  # a copy of choices that won't mutate during this function (find a better name!)
                               # used for unlock logic

    # display UCore LangPhilCult
    courses = sorted(list(choices & LANG_PHIL_CULTURE))
    if len(courses) > 0:
        print("\nLanguage, Philosophy, and Culture (3 hours, choose one course)")

    for c in courses:
        print("{:4}) {} {}".format(index, c, COURSECATALOG[c][0]))
        courseMenu[index] = c
        index += 1
    choices -= LANG_PHIL_CULTURE

    # display UCore Arts
    courses = sorted(list(choices & CREATIVE_ARTS))
    if len(courses) > 0:
        print("\nCreative Arts (3 hours, choose one course)")

    for c in courses:
        print("{:4}) {} {}".format(index, c, COURSECATALOG[c][0]))
        courseMenu[index] = c
        index += 1
    choices -= CREATIVE_ARTS

    # display UCore Social Science
    courses = sorted(list(choices & SOCIAL_SCIENCE))
    if len(courses) > 0:
        print("\nSocial/Behavioral Science (3 hours, choose one course)")

    for c in courses:
        print("{:4}) {} {}".format(index, c, COURSECATALOG[c][0]))
        courseMenu[index] = c
        index += 1
    choices -= SOCIAL_SCIENCE

    # display UCore UNI_CORE (LLC in UNI_CORE moved to CS LLC)
    courses = sorted(list(choices & UNI_CORE - LLC))
    if len(courses) > 0:
        print("\nOther University Core Requirements")

    for c in courses:
        u = prereqFor(c, coursestaken)
        print("{:4}) (prereq for {} courses) {} {}".format(index, u, c, COURSECATALOG[c][0]))
        courseMenu[index] = c
        index += 1
    choices -= UNI_CORE - LLC

    # display CS LLC
    courses = sorted(list(choices & LLC))
    if len(courses) > 0:
        print("\nComputer Science Lower-Level Core (LLC)")

    for c in courses:
        u = prereqFor(c, coursestaken)
        print("{:4}) (prereq for {} courses) {} {}".format(index, u, c, COURSECATALOG[c][0]))
        courseMenu[index] = c
        index += 1
    choices -= LLC

    # display CS other major requirements
    print("\nOther Computer Science Major Requirements")
    for c in sorted(list(choices & MAJOR_REQ)):
        u = prereqFor(c, coursestaken)
        print("{:4}) (prereq for {} courses) {} {}".format(index, u, c, COURSECATALOG[c][0]))
        courseMenu[index] = c
        index += 1
    choices -= MAJOR_REQ

    # display CS electives
    courses = choices & ELECTIVES
    if len(courses) > 0:
        print("\nComputer Science Major Electives (taken junior or senior year)")

    for c in sorted(list(choices & ELECTIVES)):
        print("{:4}) {} {}".format(index, c, COURSECATALOG[c][0]))
        courseMenu[index] = c
        index += 1
    choices -= ELECTIVES

    return courseMenu


def chooseCourses(term, courseMenu, degreeplan, coursestaken):
    '''Let the user choose courses to take for the listed term; update coursestaken
       chooseCourses(courseMenu : dict, coursestaken : set) -> coursesChosen : [course: str]
    '''
    global COURSECATALOG

    print()
    termSummary = []

    while True:
        choice = input("Select a course by number.  Press <Enter> when finished: ")
        if choice == '':
            break

        choice = int(choice) # possible runtime error
        if choice not in courseMenu:
            print("-- invalid entry --")
            continue

        course = courseMenu[choice]
        coursestaken.add(course) # this is not a pure function!

        entry = (term, course, COURSECATALOG[course][0])
        degreeplan.append(entry)

        termSummary.append("{} --> {} {}".format(term, course, COURSECATALOG[course][0]))

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
        # c[0] = term, c[1] = course rubric, c[2] = course title
        print("{:12} {:9} {}".format(c[0], c[1], c[2]))


def saveSummary(degreeplan, filename):
    '''Save the degree plan summary to a file
       saveSummary(degreeplan : [(str, str, str)]) -> NoneType (+ desired side effects)
    '''
    try:
        with open(filename, 'w') as file:
            file.write("{}{}".format('=' * 80, '\n'))
            file.write("Your degree plan summary:\n")
            file.write("{}{}".format('=' * 80, '\n'))
            file.write('\n')

            for c in degreeplan:
                # c[0] = term, c[1] = course rubric, c[2] = course title
                file.write("{:12} {:9} {}\n".format(c[0], c[1], c[2]))
    except:
        print("Couldn't write to the file!")


def main():

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

        # ask about taking summer courses, default = no
        if term.startswith('Summer'):
            summer = input("\nDo you want to take courses in the summer of {}? (y/N) ".format(term[-4:]))
            summer = summer or 'n'
            summer = summer[0].lower()
            if summer != 'y':
                term = incTerm(term)

        # display a menu of course choices for the term
        # courseMenu is a dictionary with key = choice number, value = course rubric
        courseMenu = displayChoices(term, choices, coursestaken)

        # choose courses for the term; update degreeplan; mutates coursestaken!
        degreeplan = chooseCourses(term, courseMenu, degreeplan, coursestaken)

        term = incTerm(term)

        print()

    printSummary(degreeplan)

    print("If you want to write this summary to a file, ", end="")
    filename = input("enter a filename, otherwise just press <Enter> to quit: ")
    if filename != '':
        saveSummary(degreeplan, filename)

    # THE END


# this allows this program to be imported (without executing) into a unittest script for testing
if __name__ == "__main__":
    main()


# TODO:
# - look for ways to improve the logic of functions and the whole program
# - print a nice intro and explanatory text here and there

# - test all functions

# Functions:
# good  isULC(course):
# good  prerequisites_met(course, coursestaken):
# good  LLCcomplete(coursestaken):
# good  getChoices(coursestaken):
# good  isRubric(rubric):
# good  extractRubrics(lines):
#       getCoursesTaken():
#       getTerm():
#       incTerm(term):
# ok    prereqFor(course, coursestaken):
#       displayChoices(term, choices, coursestaken):
#       chooseCourses(term, courseMenu, degreeplan, coursestaken):
# good  printSummary(degreeplan):
# good  saveSummary(degreeplan, filename):
# ok    main()
