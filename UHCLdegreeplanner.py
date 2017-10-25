# Undergraduate Catalog 2017-2018, Computer Science B.S.
# Degree Requirements: https://catalog.uhcl.edu/current/undergraduate/degrees-and-programs/bachelors/computer-science-bs

# The 2-page Computer Science degreeplan can be found at:
# https://www.uhcl.edu/academics/degrees/documents/cse/wbs-computerscience.pdf

#############
# User data #
#############

coursestaken = set() # is this needed? options should be terminal or file input


############################
# Data used by the program #
############################

def isULC(course):
    '''Given a course return True if the course is an upper-level CSCI or CENG course.
       isULC(course : str) -> bool
       Used to build the set constant ULC
       * informally tested: seems to work
    '''
    isCSCI = course[:4] == 'CSCI'   # CSCI course?
    isCENG = course[:4] == 'CENG'   # CENG course?
    isULC = course[5] in ['3', '4'] # 3000 or 4000 level course?
    return (isCSCI or isCENG) and isULC


# coursecatalog is a dictionary
#   key:   is a course rubric, 'PHYS 2325'
#   value: is a tuple, consisting of
#     - the full title of the course, "University Physics I"
#     - a set of prerequisites, {"MATH 2413"}

coursecatalog = {
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

    "CSCI 4320": ("(elective) Web Application Development", {"CSCI 2315"}),
    "CSCI 4350": ("(elective) Computer Graphics and Interface Design", {"MATH 2318",  "MATH 2413"}),
    "CSCI 4362": ("(elective) Computer Game Programming: Theory and Practice", {"CSCI 1470"}),
    "CSCI 4323": ("(elective) Computer Security", {"CSCI 1471"})}

# Language, Philosophy and Culture (3 hours required)
langPhilCulture = {"HUMN 1301", "LITR 2341", "PHIL 1301", "WGST 1301"}

# Creative Arts (3 Hours)
creativeArts = {"ARTS 1303", "ARTS 1304", "ARTS 2379"}

# Social and Behavioral Sciences (3 hours required)
socialScience = {"ANTH 2346", "CRIM 1301", "ECON 2301", "ECON 2302", "GEOG 1303", "PSYC 2301", "SOCI 1301"}


corereq = {'WRIT 1301', 'WRIT 1302', 'MATH 2413', 'PHYS 2325', 'PHYS 2326', 'HIST 1301', 'HIST 1302',
           'POLS 2305', 'POLS 2306', 'COMM 1315', 'PSYC 1100'}

majorreq = {'CHEM 1311', 'MATH 2305', 'MATH 2318', 'MATH 2414', 'MATH 2320', 'STAT 3334',
            'CSCI 1470', 'CSCI 1471', 'CSCI 3331', 'CSCI 2315', 'CSCI 3352', 'CSCI 4333', 'CSCI 3321',
            'CSCI 4354', 'CENG 3312', 'CENG 3331', 'CENG 3351', 'SWEN 4342', 'WRIT 3315', 'CSCI 4388'}

LLC = {'CSCI 1470', 'CSCI 1471', 'CSCI 2315', 'PHYS 2325', 'PHYS 2326', 'MATH 2413', 'MATH 2414', 'MATH 2305', 'WRIT 1301'}

ULC = {c for c in majorreq if isULC(c)}

CSelectives = set() # TODO: populate this set from the catalog


#################################
# Functions used by the program #
#################################

def prerequisites_met(course, coursestaken=coursestaken): # coursestaken could be removed because it is global
    '''Given a proposed course and a list of courses taken, 
       return True if the course's prerequisites have been met.
       prerequisites_met(course : str, coursestaken : set) -> bool
       * Informally tested: seems to work
    '''
    prerequisites = coursecatalog[course][1]     # get the set of prerequisites for the course

    for p in prerequisites:       # check each prerequistite
        if p not in coursestaken: # if a prerequisite is not in coursestaken
            return False          # return False

    return True                   # all prerequisites were in coursestaken


def LLCcomplete(coursestaken=coursestaken, LLC=LLC):
    '''Given a set of coursestaken and the set of LLC, return True if the LLC is complete.
       LLCcomplete(coursestaken : set, LLC : set) -> bool
    '''
    return LLC <= coursestaken # True if every element of LLC issubset of coursestaken


def possibilities(coursestaken=coursestaken,
                  corereq=corereq, majorreq=majorreq,CSelectives=CSelectives,
                  langPhilCulture=langPhilCulture, creativeArts=creativeArts,
                  socialScience=socialScience):

    # at the end of this function, possibilities will be the list of courses eligible to be taken
    # start with: corereq | majorreq | langPhilCulture | creativeArts | socialScience | CSelectives
    possibilities = corereq | majorreq | langPhilCulture | creativeArts | socialScience | CSelectives

    # remove coursestaken from possibilities
    possibilities -= coursestaken
    
    # remove courses if prerequisitives have not been met
    possibilities = {p for p in possibilities if prerequisites_met(p, coursestaken)}
    
    # remove ULC if LLC not complete
    if not LLCcomplete(coursestaken, LLC):
        possibilities -= ULC # remove ULC

    # if langPhilCulture requirement met (3 hours), remove all langPhilCulture courses from possibilities
    if len(langPhilCulture & coursestaken) > 0: # if the intersection of langPhilCulture and coursestaken is greater than zero
        possibilities -= langPhilCulture        # remove all langPhilCulture courses from the possibilities list

    # if creativeArts requirement met (3 hours), remove all creativeArts courses from possibilities
    if len(creativeArts & coursestaken) > 0: # if the intersection of creativeArts and coursestaken is greater than zero
        possibilities -= creativeArts        # remove all creativeArts courses from the possibilities list
    
    # if socialScience requirement met (3 hours), remove all socialScience courses from possibilities
    if len(socialScience & coursestaken) > 0: # if the intersection of socialScience and coursestaken is greater than zero
        possibilities -= socialScience        # remove all socialScience courses from the possibilities list

    return possibilities


def getCoursesTaken():
    '''Prompt the user to enter courses previously completed.
       getCoursesTaken() -> set'''

    coursestaken = set() # start from an empty set
    
    print("\nList courses by rubric (like CSCI 1470) that you have successfully completed.  Press <Enter> when finished.\n")

    while True:
        course = input("  Enter a course rubric: ")

        if course == '':         # the sentinel
            print()
            return coursestaken # return coursestaken to main
        
        # validate input (improve this)
        if len(course) != 9: 
            print("Use the format: CSCI 1470")
            continue

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


def displayChoices(term, courseSet):
    '''Given an unordered set of course possibilities, display and return a choice dictionary
       displayChoices(term : str, courseSet : set) -> {index: course}
    '''
    print("{}\n{} choices:\n{}".format('=' * 80, term, '=' * 80))

    choiceDict = {} # a dictionary with key = choice number, value = course rubric
    index = 1
    
    # display UCore LangPhilCult
    print("\nLanguage, Philosophy, and Culture (3 hours, choose one course)")
    for c in sorted(list(courseSet & langPhilCulture)):
        print("{:4}) {} {}".format(index, c, coursecatalog[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= langPhilCulture

    # display UCore Arts
    print("\nCreative Arts (3 hours, choose one course)")
    for c in sorted(list(courseSet & creativeArts)):
        print("{:4}) {} {}".format(index, c, coursecatalog[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= creativeArts

    # display UCore Social Science
    print("\nSocial/Behavioral Science (3 hours, choose one course)")
    for c in sorted(list(courseSet & socialScience)):
        print("{:4}) {} {}".format(index, c, coursecatalog[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= socialScience

    # display UCore corereq
    print("\nOther University Core Requirements")
    for c in sorted(list(courseSet & corereq)):
        print("{:4}) {} {}".format(index, c, coursecatalog[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= corereq
    
    # display CS LLC
    print("\nComputer Science Lower-Level Core (LLC)")
    for c in sorted(list(courseSet & LLC)):
        print("{:4}) {} {}".format(index, c, coursecatalog[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= LLC
    
    # display CS other major requirements
    print("\nOther Computer Science Major Requirements")
    for c in sorted(list(courseSet & majorreq)):
        print("{:4}) {} {}".format(index, c, coursecatalog[c][0]))
        choiceDict[index] = c
        index += 1
    courseSet -= majorreq
    
    # display CS electives
    
    return choiceDict


def chooseCourses(term, courseDict, coursestaken, degreeplan):
    '''Let the user choose courses to take for the listed term; update coursestaken
       chooseCourses(courseDict : dict, coursestaken : set) -> coursesChosen : [course: str]
    '''
    print()
    
    while True:
        choice = input("Select a course by number.  Press <Enter> when finished: ")
        if choice == '':
            break

        choice = int(choice)
        course = courseDict[choice]
        coursestaken.add(course) # this is not a pure function!

        entry = (term, course, coursecatalog[course][0])
        degreeplan.append(entry)

    return degreeplan
        
    
def main():

    degreeplan = []  # this will eventually hold the completed degree plan
    
    # let the user enter courses previously taken
    coursestaken = getCoursesTaken()

    # for testing purposes; TODO: allow reading from a file
    coursestaken = {'WRIT 1301', 'WRIT 1302', 'MATH 2413', 'LITR 2341', 'ARTS 1303', 'HIST 1301', 'HIST 1302', 'POLS 2305',
                    'COMM 1315', 'PSYC 1100', 'CHEM 1311', 'MATH 2414', 'MATH 2320'}

    term = getTerm() # let the user enter the starting term (like Fall 2017)

    while True:
        
        # a set of courses eligible to be taken
        courseSet = possibilities(coursestaken)

        # are all courses completed?
        if len(courseSet) == 0:
            break

        # display a sorted list of course choices
        courseDict = displayChoices(term, courseSet) 

        # choose courses for the term; update degreeplan; mutates coursestaken!
        degreeplan = chooseCourses(term, courseDict, coursestaken, degreeplan)

        term = incTerm(term)
        print()

    # print the summary degree plan
    print("Your degree plan:")

    insertSpace = ""
    for c in degreeplan:

        if insertSpace != c[0]: # a hack of a way to insert spaces between terms
            print()

        print("{:12} {:9} {}".format(c[0], c[1], c[2]))

        insertSpace = c[0] # remember the term so a space can be inserted before a new term

    # THE END
        

if __name__ == "__main__":
    # execute only if run as a script
    main()

# TODO:
# - test all functions
# - re-decide default arguments in functions; they're causing tricky bugs
# - look for ways to improve the logic of functions and the whole program
# - comment everything before I forget how it works!
# - unlock indicator
# - allow coursestaken to be read from a file the user inputs
# - add electives
# - write the final degree plan to a file
# - print nice intro and explanatory text here and there
# - restate the courses just selected (like the first version of this program)
