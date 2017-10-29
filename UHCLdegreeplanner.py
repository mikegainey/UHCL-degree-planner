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
#   key:   is a course rubric, 'PHYS 2325'
#   value: is a tuple, consisting of
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


UNI_CORE = {'WRIT 1301', 'WRIT 1302', 'MATH 2413', 'PHYS 2325', 'PHYS 2326', 'HIST 1301', 'HIST 1302',
           'POLS 2305', 'POLS 2306', 'COMM 1315', 'PSYC 1100'}

MAJOR_REQ = {'CHEM 1311', 'MATH 2305', 'MATH 2318', 'MATH 2414', 'MATH 2320', 'STAT 3334',
            'CSCI 1470', 'CSCI 1471', 'CSCI 3331', 'CSCI 2315', 'CSCI 3352', 'CSCI 4333', 'CSCI 3321',
            'CSCI 4354', 'CENG 3312', 'CENG 3331', 'CENG 3351', 'SWEN 4342', 'WRIT 3315', 'CSCI 4388'}

# There is some overlap with UNI_CORE
LLC = {'CSCI 1470', 'CSCI 1471', 'CSCI 2315', 'PHYS 2325', 'PHYS 2326', 'MATH 2413', 'MATH 2414', 'MATH 2305', 'WRIT 1301'}

# after this constant is built, it doesn't mutate further
ULC = {c for c in MAJOR_REQ if isULC(c)} 

ELECTIVES = {"CSCI 33x1", "CSCI 33x2", "CSCI 33x3", "CSCI 32xx"}


########################
# Function Definitions #
########################


def prerequisites_met(course, coursestaken):
    '''Given a proposed course, return True if the course's prerequisites have been met.
       prerequisites_met(course, coursestaken : set) -> bool
       * Informally tested: seems to work
    '''
    global COURSECATALOG
    
    prerequisites = COURSECATALOG[course][1]     # get the set of prerequisites for the course

    return prerequisites.issubset(coursestaken)


def LLCcomplete(coursestaken):
    '''Given the set of coursestaken and the set of LLC, return True if the LLC is complete.
       LLCcomplete(coursestaken : set, LLC : set) -> bool
    '''
    global LLC
    
    return LLC.issubset(coursestaken) # True if every element of LLC issubset of coursestaken


def getChoices(coursestaken):
    '''put a docstring here'''
    global LANG_PHIL_CULTURE
    global CREATIVE_ARTS
    global SOCIAL_SCIENCE
    global UNI_CORE
    global MAJOR_REQ
    global ULC
    global ELECTIVES

    # at the end of this function, choices will be the list of courses eligible to be taken
    # start with: UNI_CORE | MAJOR_REQ | LANG_PHIL_CULTURE | CREATIVE_ARTS | SOCIAL_SCIENCE | ELECTIVES
    choices = UNI_CORE | MAJOR_REQ | LANG_PHIL_CULTURE | CREATIVE_ARTS | SOCIAL_SCIENCE | ELECTIVES

    # remove coursestaken from choices
    choices -= coursestaken
    
    # remove courses if prerequisitives have not been met
    choices = {p for p in choices if prerequisites_met(p, coursestaken)}
    
    # remove ULC if LLC not complete
    if not LLCcomplete(coursestaken):
        choices -= ULC # remove ULC

    # if LANG_PHIL_CULTURE requirement met (3 hours), remove all LANG_PHIL_CULTURE courses from choices
    if len(LANG_PHIL_CULTURE & coursestaken) > 0: # if a LANG_PHIL_CULTURE courses has already been taken
        choices -= LANG_PHIL_CULTURE        # remove all LANG_PHIL_CULTURE courses from the choices list

    # if CREATIVE_ARTS requirement met (3 hours), remove all CREATIVE_ARTS courses from choices
    if len(CREATIVE_ARTS & coursestaken) > 0: # if the intersection of CREATIVE_ARTS and coursestaken is greater than zero
        choices -= CREATIVE_ARTS        # remove all CREATIVE_ARTS courses from the choices list
    
    # if SOCIAL_SCIENCE requirement met (3 hours), remove all SOCIAL_SCIENCE courses from choices
    if len(SOCIAL_SCIENCE & coursestaken) > 0: # if the intersection of SOCIAL_SCIENCE and coursestaken is greater than zero
        choices -= SOCIAL_SCIENCE        # remove all SOCIAL_SCIENCE courses from the choices list

    return choices


def isRubric(rubric):
    '''Given a string, return True if the string consists of 4 alpha + ' ' + 4 decimal characters
       isRubric(rubric : str) -> bool
    '''
    if len(rubric) != 9: # CSCI 1470 and other rubrics are always 9 characters
        return False
    
    words = rubric.split()

    if len(words) < 2: # make sure the line has at least 2 words: CSCI 1470 Computer Science ...
        return False

    r1 = words[0]
    if not (r1.isalpha() and len(r1) == 4): # should be 4 alphabetic characters: CSCI
        return False

    r2 = words[1]
    if not (r2.isdecimal() and len(r2) == 4): # should be 4 decimal characters: 1470
        return False

    return True


def extractRubrics(lines):
    '''Given a list of lines from a file, return a list of valid rubrics.
       extractRubrics(lines : [str]) -> [str]
    '''
    courses = []
    for line in lines:

        words = line.split()
        if len(words) < 2: # make sure the line has at least 2 words: CSCI 1470 Computer Science ...
            continue

        r1 = words[0]
        if not (r1.isalpha() and len(r1) == 4): # should be 4 alphabetic characters: CSCI
            continue

        r2 = words[1]
        if not (r2.isdecimal() and len(r2) == 4): # should be 4 decimal characters: 1470
            continue

        rubric = r1.upper() + ' ' + r2 # this should always be a well-formed rubric
        courses.append(rubric)

    return courses

    
def getCoursesTaken():
    '''Prompt the user to enter courses previously completed.
       getCoursesTaken() -> set'''

    print("\nList courses by rubric (like CSCI 1470) that you have previously completed and/or file names of files containing course rubrics.\nPress <Enter> when finished.\n")

    coursestaken = set()
    
    while True:
        course = input("  Enter a course rubric or a file name: ")

        if course == '':         # the sentinel
            return coursestaken

        # if not a valid rubric, see if it's a file name
        if not isRubric(course): # course doesn't fit the rubric pattern
            try: # check for a filename
                with open(course, 'r') as file:
                    lines = list(file)
            except:
                print("--That's not a rubric or a file name.")
                continue

            # valid filename; lines is populated; make a list of courses
            courses = extractRubrics(lines)

            # add the list of courses to coursestaken
            coursestaken |= set(courses)
            continue # don't add the filename to the set of rubrics!
            
        course = course.upper()
        coursestaken.add(course)


def getTerm():
    '''Prompt the user to enter the starting term (like Fall 2017)
       getTerm() -> str'''

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

    if nextterm.startswith('Summer'):
        summer = input("\nDo you want to take courses in the summer of {}? (y/N) ".format(nextterm[-4:]))
        summer = summer or 'n'
        summer = summer[0].lower()
        if summer != 'y':
            nextterm = incTerm(nextterm)
            
    return nextterm


# given a course, return the number of courses that that course will unlock
def unlocks(course, coursestaken):
    '''unlocks(course : str, coursestaken : set) -> int
    '''
    global COURSECATALOG
    global UNI_CORE
    global MAJOR_REQ
    global ELECTIVES
    
    coursesneeded = UNI_CORE | MAJOR_REQ | ELECTIVES - coursestaken # this is a hack if it works at all
    count = 0
    for c in coursesneeded:
        remainingPrerequisites = COURSECATALOG[c][1] - coursestaken
        a = course in remainingPrerequisites
        b = len(remainingPrerequisites) == 1
        if a and b:
            count += 1
            #print("{} will be unlocked".format(c)) # as evidence that this works
    return count


def displayChoices(term, courseSet, coursestaken):
    '''Given an unordered set of course choices, display and return a choice dictionary
       displayChoices(term : str, courseSet : set, coursetaken : set) -> {index: course}
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

    choiceDict = {} # a dictionary with key = choice number, value = course rubric
    index = 1

    courseSet2 = courseSet.copy()  # a copy of courseSet that won't mutate during this function (find a better name!)
                           # used for unlock logic
    
    # display UCore LangPhilCult
    courses = sorted(list(courseSet & LANG_PHIL_CULTURE)) 
    if len(courses) > 0:
        print("\nLanguage, Philosophy, and Culture (3 hours, choose one course)")
    
    for c in courses:
        print("{:4}) {} {}".format(index, c, COURSECATALOG[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= LANG_PHIL_CULTURE

    # display UCore Arts
    courses = sorted(list(courseSet & CREATIVE_ARTS))
    if len(courses) > 0:
        print("\nCreative Arts (3 hours, choose one course)")

    for c in courses:
        print("{:4}) {} {}".format(index, c, COURSECATALOG[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= CREATIVE_ARTS

    # display UCore Social Science
    courses = sorted(list(courseSet & SOCIAL_SCIENCE))
    if len(courses) > 0:
        print("\nSocial/Behavioral Science (3 hours, choose one course)")
        
    for c in courses:
        print("{:4}) {} {}".format(index, c, COURSECATALOG[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= SOCIAL_SCIENCE

    # display UCore UNI_CORE (LLC in UNI_CORE moved to CS LLC)
    courses = sorted(list(courseSet & UNI_CORE - LLC))
    if len(courses) > 0:
        print("\nOther University Core Requirements")
        
    for c in courses:
        u = unlocks(c, coursestaken)
        print("{:4}) (unlocks {} courses) {} {}".format(index, u, c, COURSECATALOG[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= UNI_CORE - LLC
    
    # display CS LLC
    courses = sorted(list(courseSet & LLC))
    if len(courses) > 0:
        print("\nComputer Science Lower-Level Core (LLC)")
        
    for c in courses:
        u = unlocks(c, coursestaken)
        print("{:4}) (unlocks {} courses) {} {}".format(index, u, c, COURSECATALOG[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= LLC
    
    # display CS other major requirements
    print("\nOther Computer Science Major Requirements")
    for c in sorted(list(courseSet & MAJOR_REQ)):
        u = unlocks(c, coursestaken)
        print("{:4}) (unlocks {} courses) {} {}".format(index, u, c, COURSECATALOG[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= MAJOR_REQ
    
    # display CS electives
    print("\nComputer Science Major Electives (taken junior or senior year")
    for c in sorted(list(courseSet & ELECTIVES)):
        print("{:4}) {} {}".format(index, c, COURSECATALOG[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= ELECTIVES
    
    return choiceDict


def chooseCourses(term, courseDict, degreeplan, coursestaken):
    '''Let the user choose courses to take for the listed term; update coursestaken
       chooseCourses(courseDict : dict, coursestaken : set) -> coursesChosen : [course: str]
    '''
    global COURSECATALOG
    
    print()
    minisummary = []
    
    while True:
        choice = input("Select a course by number.  Press <Enter> when finished: ")
        if choice == '':
            break

        choice = int(choice)
        if choice not in courseDict:
            print("-- invalid entry --")
            continue
        course = courseDict[choice]
        coursestaken.add(course) # this is not a pure function!

        entry = (term, course, COURSECATALOG[course][0])
        degreeplan.append(entry)

        minisummary.append("{} --> {} {}".format(term, course, COURSECATALOG[course][0]))

    print()
    for c in minisummary:
        print(c)

    degreeplan.append(('', '', '')) # a separator between terms to make output formatting easier
    return degreeplan


def printSummary(degreeplan):
    '''Print the summary degree plan
       printSummary(degreeplan : [(str, str, str)]) -> NoneType (+ desired side effects)
    '''
    print('=' * 80)
    print("Your degree plan summary:")
    print('=' * 80)
    print()

    for c in degreeplan:
        print("{:12} {:9} {}".format(c[0], c[1], c[2]))
        

def saveSummary(degreeplan, filename):
    '''Save the summary degree plan to a file
       saveSummary(degreeplan : [(str, str, str)]) -> NoneType (+ desired side effects)
    '''
    try:
        with open(filename, 'w') as file:
            file.write("{}{}".format('=' * 80, '\n'))
            file.write("Your degree plan summary:\n")
            file.write("{}{}".format('=' * 80, '\n'))
            file.write('\n')

            for c in degreeplan:
                file.write("{:12} {:9} {}\n".format(c[0], c[1], c[2]))
    except:
        print("Couldn't write to the file!")
            
        
def main():

    degreeplan = []  # this will eventually hold the completed degree plan
    
    # let the user enter courses previously taken
    coursestaken = getCoursesTaken()

    term = getTerm() # let the user enter the starting term (like Fall 2017)

    while True:
        
        # a set of courses eligible to be taken
        courseSet = getChoices(coursestaken) # uses coursestaken : set

        # are all courses completed?
        if len(courseSet) == 0:
            break

        # display a sorted list of course choices
        courseDict = displayChoices(term, courseSet, coursestaken) # uses coursestaken : set

        # choose courses for the term; update degreeplan; mutates coursestaken!
        degreeplan = chooseCourses(term, courseDict, degreeplan, coursestaken) # uses coursestaken : set

        term = incTerm(term)

        print()

    printSummary(degreeplan)

    print("If you want to write this summary to a file, ", end="")
    filename = input("enter a filename, otherwise just press <Enter> to quit: ")
    if filename != '':
        saveSummary(degreeplan, filename)
            
    # THE END
        

if __name__ == "__main__":
    # execute only if run as a script
    main()


# TODO:
# - improve variable names; settle on global variables and list them
# - re-decide default arguments in functions; they're causing tricky bugs
# - look for ways to improve the logic of functions and the whole program
# - test all functions
# - comment everything before I forget how it works!
# - print nice intro and explanatory text here and there

# - detect and print a message if user-entered rubrics are not in the COURSECATALOG
# - use re module for isRubric function
