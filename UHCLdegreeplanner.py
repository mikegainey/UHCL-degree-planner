###############################################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: CS1 Project
#
# Pseudocode:
#
###########################
# Define Global Constants #
###########################
#
#   Define a string constant welcome that has a welcome message with instructions for the user
#   Define a string constant caveat with caveat(s) for the user
#
#   Define a dictionary constant COURSECATALOG that contains information about all courses
#   applicable to the CS BS degree, where ...
#       key:   is a string representing a course number, like 'PHYS 2325'
#       value: is a tuple consisting of
#          [0] a string describing the full title of the course ('Computer Science II')
#          [1] a set of the course's prerequisites {'CSCI 1470', 'MATH 2413'}
#          [2] a set of corequisites, {'PHYS 2125'}
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
#   Define a set constant REQ_JUNIOR with courses that require junior standing
#   Define a set constant REQ_SENIOR with courses that require senior standing
#
#
#   Define a function isULC with a string parameter course
#       Set isCSCI to True if the first four characters of course is 'CSCI'
#       Set isCENG to True if the first four characters of course is 'CENG'
#       Set isULC to True if the 6th character of course is either 3 or 4
#       Return True if isCSCI or isCENG is True and isULC is True
#
# 
#   Using isULC, set ULC to the set of courses from MAJOR_REQ that satisfy isULC
#   Define a set constant ELECTIVES to represent Major Elective courses
#
#
########################
# Function Definitions #
########################
#
#
#   Define a function prerequisites_met that takes parameters course and coursestaken:
#       Set prerequisites to the set of the course's prerequisites found in COURSECATALOG
#       Return True if prerequisites is a subset of coursestaken
#
#
#   Define a function LLCcomplete that takes a parameter coursestaken:
#       Return True if LLC is a subset of coursestaken
#
#
#   Define a function getChoices that takes a parameter coursestaken:
#       Set choices to the union of UNI_CORE, MAJOR_REQ, LANG_PHIL_CULTURE, CREATIVE_ARTS,
#         SOCIAL_SCIENCE, and ELECTIVES.
#       Remove coursestaken from choices.
#       Remove courses with unmet prerequisites from choices.
#       If LLC is not complete:
#           remove ULC and ELECTIVES from choices.
#       Set standing to the student's standing and total semester hours using the classification function.
#       If standing is not junior or senior, remove courses in the REQ_JUNIOR and ELECTIVES sets
#       If standing is not senior, remove courses in the REQ-SENIOR set
#
#       Begin a loop that executes twice:
#           Begin a loop over a copy of choices with the lcv course:
#               Set corequisites to course's corequisites
#               If course doesn't have any corequisites, continue the loop
#               If at least one of the corequisites is in coursestaken, continue the loop
#               If the course's corequisites are not in choices, remove the course from choices
#
#       If the length of the intersection of LANG_PHIL_CULTURE and coursestaken is greater than zero:
#           remove LANG_PHIL_CULTURE from choices.
#       If the length of the intersection of CREATIVE_ARTS and coursestaken is greater than zero:
#           remove CREATIVE_ARTS from choices.
#       If the length of the intersection of SOCIAL_SCIENCE and coursestaken is greater than zero:
#           remove SOCIAL_SCIENCE from choices.
#       Return choirs to the calling function/program.
#
#
#   Define a function isCourseNumber that takes a string parameter maybeCourseNumber:
#       If the length of maybeCourseNumber is not 9, return False.
#       Set words to a list made from splitting maybeCourseNumber into words
#       If the length of words is less than 2, return False.
#       Set part1 to the first word of words.
#       If part1 is either not all alphabetic or not of length 4, return False.
#       Set part2 to the second word of words.
#       If part2 is either not all decimal or not of length 4, return False.
#       Return True
#
#
#   Define a function extractCourseNumbers that takes a parameter lines that is a list of strings
#       Set courses to an empty list.
#       Begin a loop iterating through the elements of lines using the lcv line
#           If the length of line is less than 9, skip the rest of the loop
#           Set maybeCourseNumber to the first 9 characters of line
#           If maybeCourseNumber returns False when passed to isCourseNumber, skip the rest of the loop
#           Set courseNumber to maybeCourseNumber and ensure all uppercase
#           Append courseNumber to courses
#       Return courses to the calling program/function
#
#
#   Define a function add2CoursesTaken with parameters course and coursestaken:
#       If course is in coursestaken ...
#           print a message that it was already added and return to the calling function
#       If course is not in COURSECATALOG:
#           print a message saying the course is not recognized as a requirement for the CS BS degree
#           and return to the calling function
#       Add course to coursestaken
#       Print a message that course was added
#
#
#   Define a function getCoursesTaken:
#       Prompt the user to enter courses (like CSCI 1470) previously completed or a file with a list of courses completed
#       Set coursestaken to the empty set.
#       Begin a loop to get user input.
#           Set course to the user's input.
#           If the user just pressed <Enter>, return coursestaken to the calling program/function.
#           If isCourseNumber returns True with course as the argument,
#               convert course to all uppercase, and
#               pass course and coursestaken to add2CoursesTaken.
#           else,
#               Try to open a file for reading named course
#               If successful, set lines to the list of lines in the file
#               Otherwise, print a message "That's not a course or a file name"
#               and continue the loop
#
#               Set courses to the return value of extractCourseNumbers with argument lines.
#               Begin a loop iterating over courses with lcv course:
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
#       Set coursesneeded to the union of UNI_CORE and MAJOR_REQ
#       If the length of the intersection of LANG_PHIL_CULTURE and coursestaken is zero,
#           Add LANG_PHIL_CULTURE to coursesneeded
#       Set count to zero
#       Begin a loop iterating over coursesneeded with lcv c
#           Set prerequisites to the set of prerequisites for c
#           If the parameter course is in prerequisites, increment count
#       Return count
#
#
#   Define a function countHours that takes a parameter courses:
#       Set totalHours to zero
#       Begin a loop iterating over courses with lcv course:
#           Increment totalHours by the number of semester hours of the current course
#       Return totalHours to the calling function
#
#
#   Define a function classification that takes a parameter coursestaken:
#       Set totalHours using the countHours function with coursestaken as the argument
#       If totalHours is less than or equal to 29, then set standing to 'freshman'
#       else if totalHours is between 30 and 59, then set standing to 'sophomore'
#       else if totalHours is between 60 and 89, then set standing to 'junior'
#       else, set standing to 'senior'
#       Return a tuple with standing and totalHours to the calling function
#
#
#   Define a function flipLabOrder with a parameter choices:
#       Begin a loop from zero to the length of choices minus one with lcv c:
#           Set c1 to the cth element of choices
#           Set c2 to the (c+1)th element of choices
#           If c1 and c2 are not the same except for the "hours" digit, continue the loop
#           If not the hours digit of c1 is '1' and the hours digit of c2 is '3', continue the loop
#           Swap c1 and c2 in choices
#       Return choices to the calling function
#
#
#   Define a function displayChoices with parameters term, choices, and coursestaken:
#       Set runningChoices to a copy of choices
#       Set standing to the return value of classification given the argument coursestaken
#
#       Display a header for the term
#       Set courseMenu to an empty dictionary
#       Set index to 1
#
#       Set categoryChoices to a sorted list of the intersection of runningChoices and LANG_PHIL_CULTURE
#       If the length of categoryChoices is greater than zero, display a LANG_PHIL_CULTURE heading
#       Begin a loop over categoryChoices with lcv course:
#           Display index, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove LANG_PHIL_CULTURE from runningChoices
#
#       Set categoryChoices to a sorted list of the intersection of runningChoices and CREATIVE_ARTS
#       If the length of categoryChoices is greater than zero, display a CREATIVE_ARTS heading
#       Begin a loop over categoryChoices with lcv course:
#           Display index, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove CREATIVE_ARTS from runningChoices
#
#       Set categoryChoices to a sorted list of the intersection of runningChoices and SOCIAL_SCIENCE
#       If the length of categoryChoices is greater than zero, display a SOCIAL_SCIENCE heading
#       Begin a loop over categoryChoices with lcv course:
#           Display index, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove SOCIAL_SCIENCE from runningChoices
#
#       Set categoryChoices to a sorted list of the intersection of runningChoices and UNI_CORE minus LLC
#       If the length of categoryChoices is greater than zero, display a University Core heading
#       Begin a loop over categoryChoices with lcv course:
#           Set isPrereqFor to the return value of prereqFor with arguments course and coursestaken
#           Display index, isPrereqFor, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove UNI_CORE from runningChoices
#
#       Set categoryChoices to a sorted list of the intersection of runningChoices and LLC
#       If the length of categoryChoices is greater than zero, display a CS Lower-Level Core heading
#       Set categoryChoices to the return value of flipLabOrder with argument categoryChoices
#       Begin a loop over categoryChoices with lcv course:
#           Set isPrereqFor to the return value of prereqFor with arguments course and coursestaken
#           Display index, isPrereqFor, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove LLC from runningChoices
#
#       Set categoryChoices to a sorted list of the intersection of runningChoices and MAJOR_REQ
#       If the length of categoryChoices is greater than zero, display a CS Major Requirements heading
#       Set categoryChoices to the return value of flipLabOrder with argument categoryChoices
#       Begin a loop over categoryChoices with lcv course:
#           Set isPrereqFor to the return value of prereqFor with arguments course and coursestaken
#           Display index, isPrereqFor, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove MAJOR_REQ from runningChoices
#
#       If 'CSCI 4388' is in categoryChoices, ...
#           print a message that CSCI 4388 may be taken only during the final semester before graduation
#       
#       Set categoryChoices to a sorted list of the intersection of runningChoices and ELECTIVES
#       If the length of categoryChoices is greater than zero, display a CS Major Electives heading
#       Begin a loop over categoryChoices with lcv course:
#           Display index, course, and the name of the course
#           Add course to courseMenu with key index
#           Add 1 to index
#       Remove ELECTIVES from runningChoices
#       Verify that runningChoices is empty
#
#       Return courseMenu to the calling program/function
#
#
#   Define a function checkCorequisites with a parameter courses:
#       Set unselectedCorequisiteList to the empty list
#       Begin a loop over courses with lcv course:
#           Set corequisites to course's corequisites
#           Set unselectedCorequisites to corequisites minus courses
#           If the length of unselectedCorequisites is greater than zero, ...
#               Append to unselectedCorequisiteList a tuple with course and unselectedCorequisites
#           Return unselectedCorequisiteList
#
#
#   Define a function chooseCourses with parameters term, choices, coursestaken, and degreeplan:
#       Begin a loop to verify that corequisite requirements are met:
#           Set courseMenu to the return value of displayChoices with arguments term, choices, and coursestaken
#           Set courses to the empty list
#               Begin a loop to get user input:
#                   Set choice from a user prompt to select a course by number, pressing <Enter> when finished
#                   If the user just presses <Enter>, exit the loop
#                   If choice is not a decimal character,
#                       print an error message and go to the beginning of the loop
#                   Cast choice to an integer
#                   If choice is not in courseMenu,
#                       display an error message and go to the beginning of the loop
#                   Set course to courseMenu with index choice
#                   If course is not in courses,
#                       append course to courses
#
#               If courses is empty,
#                   return degree plan to the calling function
#               Begin a loop over courses with lcv course:
#                   Print term, course, and the course title from COURSECATALOG
#               Print the term and total semester hours in courses using the countHours function
#
#               Set unselectedCorequisites to the return value of checkCorequisites with argument courses
#               If unselectedCorequisites is empty,
#                   Set accept to user input with prompt "Do you want to accept these courses?"
#                   If the user just presses <Enter>, set accept to 'y'
#                   Make accept lowercase
#                   If accept is 'y'
#                       break out of the loop
#                   else,
#                       continue the loop so the user can reselect courses for this term
#               else,
#                   print a message, "You have selected a course without selecting its corequisite!"
#                   Begin a loop over unselectedCorequisites with lcvs c and uc
#                       Set unselCoreq to values in uc joined with '&'
#                       Print c requires unselCoreq
#
#                   Set accept to user input with prompt, "Do you want to reselect courses for this term?"
#                   If the user just presses <Enter>, set accept to 'y'
#                   Make accept lowercase
#                   If accept is 'n'
#                       break out of the loop accepting the selected courses
#                   else,
#                       continue the loop and reselect courses
#
#           Begin a loop over courses with lcv course:
#               Add course to coursestaken
#               Set entry to a tuple consisting of term, course, and course title from COURSECATALOG
#               Append entry to degreeplan
#           Append a blank tuple to degreeplan
#           Return degreeplan to the calling function
#
#
#   Define a function printSummary with parameter degreeplan:
#       Set standing to the return value of classification with argument coursestaken
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
#       Set standing to the return value of classification with argument coursestaken
#       Try to open filename for writing
#           Write a heading, "Your degree plan summary"
#           Begin a loop over degreeplan with lcv c:
#               Write all three elements of c
#           Display a message, filename "contains your degree plan summary"
#       If unsuccessful, print a message, "couldn't write to the file"
#
#
#   Define a function main:
#       Print the contents of welcome
#       Set degreeplan to the empty list
#       Set coursestaken to the return value of getCoursesTaken
#       Set term to the return value of getTerm
#       Begin a loop:
#           Set choices to the return value of getChoices with argument coursestaken
#           If the length of choices is zero, exit the loop
#           Set term to the return value of summerTerm with argument term
#           Set degreeplan to the return value of chooseCourses with arguments term, choices, coursestaken, and degreeplan
#           Set term to the return value of incTerm with argument term
#       Call the printSummary function with arguments degreeplan and coursestaken
#       Call the saveSummary function with arguments degreeplan and coursestaken
#
#
#   If the name of the running module is '__main__' then call the main function
#
###############################################################################

# UNDERGRADUATE Catalog 2017-2018, Computer Science B.S.
# Degree Requirements: https://catalog.uhcl.edu/current/undergraduate/degrees-and-programs/bachelors/computer-science-bs

# The 2-page Computer Science degreeplan can be found at:
# https://www.uhcl.edu/academics/degrees/documents/cse/wbs-computerscience.pdf


###########################
# Define Global Constants #
###########################

welcome = '''================================================================================
                   UHCL Computer Science B.S. Degree Planner
================================================================================

If you are a UHCL Computer Science B.S. student, this program will help you
choose courses to take next term and each successive term until graduation.

First, tell the program the courses you have already completed.  You can enter
them one-at-a-time at the keyboard and/or you can enter a file name with a list
of courses.

Put the file in the same folder as the program.  In the file, list course
numbers (like CSCI 1470) one-per-line.  Anything on the line after the course
number will be ignored so you can include notes after course numbers or on
separate lines.

After entering your starting term, you will see a menu of courses that you are
eligible to take.  Choose courses for the term by menu number.  The program will
then restate your choices and ask you to verify them before moving to the next
term.

Next to many courses in the list, there will be something that looks like
"(prereq for # courses)."  It shows that the listed course is a prerequisite for
the given number of other courses.  Since you can't take those other courses
until this course is completed, it's a good idea to prioritize taking courses
that are prerequisites for others.  Calculus I is a good example.  You should
also prioritize courses in the Lower-Level Core since upper-level CSCI and CENG
courses can't be taken until the LLC is complete.

After you have chosen all of your courses, the program will display your
complete degree plan summary.  If you enter a file name, the summary will be
saved as a text file in the same folder as the program.
================================================================================'''

caveat = '''Note: This program uses course information and degree requirements from the
UHCL 2017-2018 undergraduate catalog.  Refer to your personal CPS for the
requirements that apply to you.'''

# COURSECATALOG is a dictionary where
#   key:   is a string representing a course number, like 'PHYS 2325'
#   value: is a tuple consisting of
#     [0] a string describing the full title of the course, "University Physics I"
#     [1] a set of prerequisites, {"MATH 2413", "MATH 2414"}
#     [2] a set of corequisites, {"PHYS 2125"}

COURSECATALOG = {
    # Communication (6 hours)
    "WRIT 1301": ("Composition I", set(), set()),
    "WRIT 1302": ("Composition II", {"WRIT 1301"}, set()),

    # Mathematics (4 hours), # this has a prerequisite, but it's not part of the degree requirements
    "MATH 2413": ("Calculus I", set(), set()),

    # Life and Physical Sciences (6 hours)
    "PHYS 2325": ("University Physics I", {"MATH 2413"}, {"PHYS 2125"}),
    "PHYS 2125": ("University Physics I Lab", set(), {"PHYS 2325"}),
    "PHYS 2326": ("University Physics II", {"MATH 2414", "PHYS 2325"}, {"PHYS 2126"}),
    "PHYS 2126": ("University Physics II Lab", set(), {"PHYS 2326"}),

    # Language, Philosophy and Culture (3 hours)
    "HUMN 1301": ("Humanities", set(), set()),
    "LITR 2341": ("Literature and Experience", {"WRIT 1301"}, set()),
    "PHIL 1301": ("Introduction to Philosophy", set(), set()),
    "WGST 1301": ("Gender Matters: Introduction to Women's and Gender Studies", set(), set()),

    # Creative Arts (3 Hours)
    "ARTS 1303": ("World Art Survey I", set(), set()),
    "ARTS 1304": ("World Art Survey II", set(), set()),
    "ARTS 2379": ("Arts and the Child", set(), set()),

    # American History (6 hours)
    "HIST 1301": ("United States History I", set(), set()),
    "HIST 1302": ("United States History II", set(), set()),

    # Government/Political Science (6 hours)
    "POLS 2305": ("Federal Government", set(), set()),
    "POLS 2306": ("Texas Government", set(), set()),

    # Social and Behavioral Sciences (3 hours)
    "ANTH 2346": ("General Anthropology", set(), set()),
    "CRIM 1301": ("Introduction to Criminal Justice", set(), set()),
    "ECON 2301": ("Principles of Macroeconomics", set(), set()),
    "ECON 2302": ("Principles of Microeconomics", set(), set()),
    "GEOG 1303": ("World Regional Geography", set(), set()),
    "PSYC 2301": ("Introduction to Psychology", set(), set()),
    "SOCI 1301": ("Introduction to Sociology", set(), set()),

    # Component Area Option (6 hours)
    "COMM 1315": ("Public Speaking", set(), set()),
    "PSYC 1100": ("Learning Frameworks", set(), set()),

    # Major Requirements (67 hours)
    "CHEM 1311": ("General Chemistry I", set(), {"CHEM 1111"}),
    "CHEM 1111": ("General Chemistry I Lab", set(), {"CHEM 1311"}),
    "MATH 2305": ("Discrete Mathematics", {"MATH 2413"}, set()),
    "MATH 2318": ("Linear Algebra", {"MATH 2413"}, set()),
    "MATH 2414": ("Calculus II", {"MATH 2413"}, set()),
    "MATH 2320": ("Differential Equations", {"MATH 2414"}, set()),
    "STAT 3334": ("Probability & Statistics for Scientists & Engineers", {"MATH 2413", "MATH 2414"}, set()),
    "CSCI 1470": ("Computer Science I", set(), set()),
    "CSCI 1471": ("Computer Science II", {"CSCI 1470"}, set()), # MATH 2413 was a prereq in the 2016-17 catalog
    "CSCI 3331": ("Computer Organization & Assembly Language", {"CSCI 2315", "MATH 2305", "MATH 2414",
                                                                "PHYS 2325",  "PHYS 2326"}, set()),
    "CSCI 2315": ("Data Structures", {"CSCI 1471"}, set()),
    "CSCI 3352": ("Advanced Data Structures", {"CSCI 2315", "MATH 2305", "MATH 2414", "PHYS 2325", "PHYS 2326"}, set()),
    "CSCI 4333": ("Design of Database Systems", {"CSCI 2315"}, set()),
    "CSCI 3321": ("Numerical Methods", {"MATH 2318", "MATH 2320", "CSCI 1471"}, set()),
    "CSCI 4354": ("Operating Systems         (take with CENG 3351)", # requires senior level standing
                  {"CSCI 2315", "CSCI 3331", "MATH 2305", "MATH 2414", "PHYS 2325", "PHYS 2326"}, {"CENG 3351"}),

    "CENG 3312": ("Digital Circuits", {"MATH 2414", "PHYS 2326"}, {"CENG 3112"}),
    "CENG 3112": ("Digital Circuits Lab", set(), {"CENG 3312"}),
    
    "CENG 3331": ("Intro to Telecommunications and Networks",  {"CENG 3312"}, {"CENG 3131"}),
    "CENG 3131": ("Intro to Telecommunications and Networks Lab",  set(), {"CENG 3331"}),

    # prereq changed from 2016-17
    "CENG 3351": ("Computer Architecture     (take with CSCI 4354)", {"CENG 3331"}, {"CENG 3151", "CSCI 4354"}), 
    "CENG 3151": ("Computer Architecture Lab", {"CENG 3312", "CENG 3112"}, {"CENG 3351"}),

    "SWEN 4342": ("Software Engineering", {"CSCI 1470", "CSCI 2315"}, set()), # CSCI 1470 prereq implied; CSCI 2315 recommended
    "WRIT 3315": ("Advanced Technical Writing", {"WRIT 1301", "WRIT 1302"}, set()), # requires junior level standing
    "CSCI 4388": ("Senior Project in Computer Science", {"CSCI 3352", "SWEN 4342"}, set()),

    # CSCI/CINF Major Electives; taken junior or senior year
    "CSCI 33x1": ("CSCI/CINF 33xx or 43xx upper level elective", set(), set()),
    "CSCI 33x2": ("CSCI/CINF 33xx or 43xx upper level elective", set(), set()),
    "CSCI 33x3": ("CSCI/CINF 33xx or 43xx upper level elective", set(), set()),
    "CSCI 33x4": ("CSCI/CINF 32xx or 42xx upper level elective", set(), set())}

# Language, Philosophy and Culture (3 hours required)
LANG_PHIL_CULTURE = {"HUMN 1301", "LITR 2341", "PHIL 1301", "WGST 1301"}

# Creative Arts (3 hours required)
CREATIVE_ARTS = {"ARTS 1303", "ARTS 1304", "ARTS 2379"}

# Social and Behavioral Sciences (3 hours required)
SOCIAL_SCIENCE = {"ANTH 2346", "CRIM 1301", "ECON 2301", "ECON 2302", "GEOG 1303", "PSYC 2301", "SOCI 1301"}

# University Core
UNI_CORE = {'WRIT 1301', 'WRIT 1302', 'MATH 2413', 'PHYS 2325', 'PHYS 2125', 'PHYS 2326', 'PHYS 2126',
            'HIST 1301', 'HIST 1302', 'POLS 2305', 'POLS 2306', 'COMM 1315', 'PSYC 1100'}

# Major Requirements
MAJOR_REQ = {'CHEM 1311', 'CHEM 1111', 'MATH 2305', 'MATH 2318', 'MATH 2414', 'MATH 2320', 'STAT 3334',
             'CSCI 1470', 'CSCI 1471', 'CSCI 3331', 'CSCI 2315', 'CSCI 3352', 'CSCI 4333', 'CSCI 3321',
             'CSCI 4354', 'CENG 3312', 'CENG 3112', 'CENG 3331', 'CENG 3131', 'CENG 3351', 'CENG 3151',
             'SWEN 4342', 'WRIT 3315', 'CSCI 4388'}

# CS Lower-Level Core; note there is some overlap with UNI_CORE
LLC = {'CSCI 1470', 'CSCI 1471', 'CSCI 2315', 'PHYS 2325', 'PHYS 2125', 'PHYS 2326', 'PHYS 2126',
       'MATH 2413', 'MATH 2414', 'MATH 2305', 'WRIT 1301'}

# requires junior standing; getChoices requires LLC complete and junior or senior standing to allow electives
REQ_JUNIOR = {'WRIT 3315'}

# requires senior standing
REQ_SENIOR = {'CSCI 4354', 'CSCI 4388'} # CSCI 4388 should be taken in the final semester before graduation

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


# Major electives; modified the last digit because course numbers must be unique
ELECTIVES = {"CSCI 33x1", "CSCI 33x2", "CSCI 33x3", "CSCI 33x4"}


########################
# Function Definitions #
########################


def prerequisites_met(course, coursestaken):
    '''Given a course and courses taken, return True if the course's prerequisites have been met.
       prerequisites_met(course : str, coursestaken : set) -> bool
    '''
    # get the set of prerequisites for the course
    prerequisites = COURSECATALOG[course][1] 

    # return True if every element of prerequisites is in coursestaken
    return prerequisites.issubset(coursestaken) 


def LLCcomplete(coursestaken):
    '''Given the set of courses taken, return True if the CS LLC is complete.
       LLCcomplete(coursestaken : set) -> bool
    '''
    # return True if every element of LLC issubset of coursestaken
    return LLC.issubset(coursestaken) 


def getChoices(coursestaken):
    '''Given the set of courses taken, return the set of courses eligible to be taken (choices)
       getChoices(coursestaken : set) -> set
    '''
    # at the end of this function, choices will be the list of courses eligible to be taken
    choices = UNI_CORE | MAJOR_REQ | LANG_PHIL_CULTURE | CREATIVE_ARTS | SOCIAL_SCIENCE | ELECTIVES

    # remove coursestaken from choices
    choices -= coursestaken

    # remove courses where prerequisites have not been met
    choices = {course for course in choices if prerequisites_met(course, coursestaken)}

    # remove ULC and ELECTIVES if LLC not complete
    if not LLCcomplete(coursestaken):
        choices -= (ULC | ELECTIVES) # remove ULC and ELECTIVES

    # determine standing, a tuple: (classification, total hours)
    standing = classification(coursestaken)
    
    # remove REQ_JUNIOR if not junior or senior standing (removes electives and WRIT 3315)
    if standing[0] not in {'junior', 'senior'}:
        choices -= (REQ_JUNIOR | ELECTIVES)
    
    # remove CSCI 4354 (the only course in REQ_SENIOR) if not senior standing
    if standing[0] != 'senior':
        choices -= REQ_SENIOR

    # remove a course if its corequisites are not choices, UNLESS a corequisite has already been taken
    for course in choices.copy():

        # this can happen because elements of choices are being removed while the copy stays the same
        if course not in choices:
            continue

        # if the course doesn't have corequisites, there is nothing to do
        corequisites = COURSECATALOG[course][2]
        if len(corequisites) == 0:
            continue

        # if at least one of the corequisites is in coursestaken, show the lone corequisite; continue the loop
        if len(corequisites & coursestaken) > 0:
            continue

        # finally, if corequisite(s) are not in choices, remove the course and any other corequisites
        if not corequisites.issubset(choices):
            choices.remove(course)
            choices -= corequisites
            
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


def isCourseNumber(maybeCourseNumber):
    '''Given a string, return True if the string consists of 4 alpha + ' ' + 4 decimal characters
       isCourseNumber(maybeCourseNumber : str) -> bool
       the alpha characters can be uppercase or lowercase
    '''
    # course numbers are always 9 characters (like 'CSCI 1470')
    if len(maybeCourseNumber) != 9: 
        return False

    words = maybeCourseNumber.split()

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


def extractCourseNumbers(lines):
    '''Given a list of lines from a file, return an ordered list of valid course numbers.
       extractCourseNumbers(lines : [str]) -> [str]
       These course numbers might not apply to the CS BS degree (checked in add2CoursesTaken)
    '''
    courses = list()
    for line in lines:

        # the line is too short to contain a course number
        if len(line) < 9:             
            continue

        # the part of the line to check
        maybeCourseNumber = line[:9]        

        # if not a course number, loop back
        if not isCourseNumber(maybeCourseNumber): 
            continue

        # at this point, it's a confirmed course number (format)
        courseNumber = maybeCourseNumber          
        courseNumber = courseNumber.upper()

        # add the course number to the output list
        courses.append(courseNumber)        

    return courses


def add2CoursesTaken(course, coursestaken):
    '''Add a course to coursestaken only if it applies to the CS BS degree
       add2CoursesTaken(course : str, coursestaken : set) -> NoneType (+ mutating coursestaken)
       used twice in getCoursesTaken (so this function prevents code duplication)
    '''
    if course in coursestaken:
        print("----- {} was already added".format(course))
        return

    if course not in COURSECATALOG:
        print("----- {} not recognized as a requirement for the Computer Science B.S. degree".format(course))
        return
    
    coursestaken.add(course)
    print("added {} {}".format(course, COURSECATALOG[course][0]))


def getCoursesTaken():
    '''Prompt the user to enter courses previously completed and/or load courses from file(s).
       getCoursesTaken() -> NoneType (+ calling add2CoursesTaken mutator function)'''

    print("\nEnter course numbers (like CSCI 1470) that you have previously completed and/or")
    print("the name of a file containing course numbers (or just press <Enter>).\n")

    coursestaken = set()

    while True:
        course = input("Enter a course number or a file name. Press <Enter> when finished: ")

        # the sentinel
        if course == '':
            return coursestaken

        # the input string is a course number
        if isCourseNumber(course):
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
            courses = extractCourseNumbers(lines)
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


def countHours(courses):
    '''Given a list or set of courses, return the total number of semester credit hours.
       countHours(courses : [str] or {str} ) -> int
       classification gives this function a set; chooseCourses gives it a list; Python can handle it!
    '''
    totalHours = 0
    for course in courses:
        totalHours += int(course[-3]) # "CSCI 1470"[-3] = 4

    return totalHours


def classification(coursestaken):
    '''Given coursestaken, return a tuple with (classification, total hours completed) where classification is ...
       freshman for 1-29 hours, sophomore for 30-59 hours, junior for 60-89 hours, and senior for 90+ hours
       classification(coursestaken : set) -> (str, int)
    '''
    # count the semester credit hour total in coursestaken
    totalHours = countHours(coursestaken)
    
    # determine the classification from totalHours
    if totalHours <= 29:
        standing = 'freshman'
    elif 30 <= totalHours <= 59:
        standing = 'sophomore'
    elif 60 <= totalHours <= 89:
        standing = 'junior'
    else:
        standing = 'senior'

    return (standing, totalHours)


def flipLabOrder(choices):
    '''Given a list of courses sorted by course number, move labs from before to after their main course in the list.
       flipLabOrder(choices : [str]) -> [str]
       Otherwise, labs would always precede their main course in the course menu: (e.g. 2125 comes before 2325).
    '''
    for c in range(len(choices) -1):
        c1 = choices[c]
        c2 = choices[c+1]

        # check if course numbers are the same except for the "hours" digit; if not, continue
        if (c1[:6] + c1[-2:]) != (c2[:6] + c2[-2:]):
            continue

        # check for a 1 hour course followed by a 3 hour course; if not, continue
        if not (c1[6] == '1' and c2[6] == '3'):
            continue

        # a lab precedes its main course; swap their order
        choices[c], choices[c+1] = choices[c+1], choices[c]

    return choices
    

def displayChoices(term, choices, coursestaken):
    '''Given a set of course choices, display and return a choice dictionary (menu)
       displayChoices(term : str, choices : set, coursestaken : set) -> {index: course}
    '''
    # set up a variable that can mutate (so choices can be preserved)
    runningChoices = choices.copy() # make a copy of choices!
    
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
    categoryChoices = sorted(list(runningChoices & LANG_PHIL_CULTURE))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nLanguage, Philosophy, and Culture (3 hours, choose one course)")

    for course in categoryChoices:
        print("{:4}) {} {}".format(index, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    runningChoices -= LANG_PHIL_CULTURE

    # display Creative Arts courses
    categoryChoices = sorted(list(runningChoices & CREATIVE_ARTS))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nCreative Arts (3 hours, choose one course)")

    for course in categoryChoices:
        print("{:4}) {} {}".format(index, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    runningChoices -= CREATIVE_ARTS

    # display Social Science courses
    categoryChoices = sorted(list(runningChoices & SOCIAL_SCIENCE))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nSocial/Behavioral Science (3 hours, choose one course)")

    for course in categoryChoices:
        print("{:4}) {} {}".format(index, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    runningChoices -= SOCIAL_SCIENCE

    # display UCore UNI_CORE choices (LLC in UNI_CORE is listed in CS LLC)
    categoryChoices = sorted(list(runningChoices & UNI_CORE - LLC))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nOther University Core Requirements")

    for course in categoryChoices:
        isPrereqFor = prereqFor(course, coursestaken)
        print("{:4}) (prereq for {} courses) {} {}".format(index, isPrereqFor, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    runningChoices -= UNI_CORE - LLC # check this for correctness! I think it's right.

    # display CS LLC choices
    categoryChoices = sorted(list(runningChoices & LLC))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nComputer Science Lower-Level Core (LLC)")

    # flip the order of courses and labs (so the course comes before its lab)
    categoryChoices = flipLabOrder(categoryChoices)

    for course in categoryChoices:
        isPrereqFor = prereqFor(course, coursestaken)
        print("{:4}) (prereq for {} courses) {} {}".format(index, isPrereqFor, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    runningChoices -= LLC

    # display CS other major requirements choices
    categoryChoices = sorted(list(runningChoices & MAJOR_REQ))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nOther Computer Science Major Requirements")

    # flip the order of courses and labs (so the course comes before its lab)
    categoryChoices = flipLabOrder(categoryChoices)
        
    for course in categoryChoices:
        isPrereqFor = prereqFor(course, coursestaken)
        print("{:4}) (prereq for {} courses) {} {}".format(index, isPrereqFor, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    runningChoices -= MAJOR_REQ

    # if CSCI 4388 is a choice, print  "CSCI 4388 may be taken only during the final semester before graduation."
    if 'CSCI 4388' in categoryChoices:
        print("\n   Note: CSCI 4388 may be taken only during the final semester before graduation.")

    # display CS electives
    categoryChoices = sorted(list(runningChoices & ELECTIVES))
    if len(categoryChoices) > 0: # don't display the heading if this requirement has been met
        print("\nComputer Science Major Electives")

    for course in categoryChoices:
        # assuming CS electives aren't going to be prerequisites for anything else
        print("{:4}) {} {}".format(index, course, COURSECATALOG[course][0]))
        courseMenu[index] = course # build the course menu
        index += 1
    runningChoices -= ELECTIVES

    assert runningChoices == set() # runningChoices should be empty at this point

    return courseMenu


def checkCorequisites(courses):
    '''Given a list of courses chosen for a term, return a list of tuples: (course, { set of unselected corequisite(s)})
       representing courses and their unselected corequisites; The course is listed only if there are unselected corequisites.
       checkCorequisites(courses : [str]) -> [(str, {set of str})]
    '''
    unselectedCorequisiteList = []

    for course in courses:
        corequisites = COURSECATALOG[course][2]
        unselectedCorequisites = corequisites - set(courses) # the unselected corequisite courses
        if len(unselectedCorequisites) > 0:
            unselectedCorequisiteList.append((course, unselectedCorequisites))

    return unselectedCorequisiteList


def chooseCourses(term, choices, coursestaken, degreeplan):
    '''Let the user choose courses to take for the listed term; update coursestaken
       chooseCourses(courseMenu : dict, coursestaken : set) -> coursesChosen : [course: str]
       ... and coursestaken is also updated
    '''
    while True: # the loop to verify that corequisite requirements are met

        # create and display a menu of course choices for the term
        courseMenu = displayChoices(term, choices, coursestaken)
        print()

        courses = [] # a list of courses chosen for that term only

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

            # the chosen course
            course = courseMenu[choice] # course is a course number
            if course not in courses:
                courses.append(course) # the tentative list of courses for this term

        # if no courses were chosen, just return
        if len(courses) == 0:
            return degreeplan
    
        # Print the term summary
        print()
        for course in courses:
            print("{} --> {} {}".format(term, course, COURSECATALOG[course][0]))

        # display the semester credit hour total for the term
        print('=' * 80)
        print("{} --> {} semester hours".format(term, countHours(courses)))
        
        # unselectedCorequisites is a list of tuples: [(course, set of unselected corequisite courses)]
        unselectedCorequisites = checkCorequisites(courses)

        if not unselectedCorequisites:
            # corequisite requirements are met
            accept = input("\nDo you want to accept these courses and continue to the next term? (Y/n): ")
            accept = accept or 'y'
            accept = accept[0].lower()
            if accept == 'y': 
                break    # accept courses selections
            else:
                print()
                continue # re-select courses
        else:
            # print a warning about unselected corequisites
            print()
            print("You have selected a course without selecting its corequisite!")
            for c, uc in unselectedCorequisites:
                unselCoreq = ' & '.join(uc)
                print("  {} requires {}".format(c, unselCoreq))
                
            # ask the user to reselect courses that meet corequisite requirements
            accept = input("\nDo you want to reselect courses for this term? (Y/n): ")
            accept = accept or 'y'
            accept = accept[0].lower()
            if accept == 'n': # user wants to accept courses in spite of not meeting corequisite requirement
                break
            else:
                print()
                continue # re-select courses
            

    # add the selected courses to coursestaken and degreeplan
    for course in courses:
        coursestaken.add(course) # this mutates coursestaken
        entry = (term, course, COURSECATALOG[course][0])
        degreeplan.append(entry)

    degreeplan.append(('', '', '')) # a separator between terms to make output formatting easier
    return degreeplan


def printSummary(degreeplan, coursestaken):
    '''Print the degree plan summary, the final output
       printSummary(degreeplan : [(str, str, str)]) -> NoneType (+ desired side effects)
    '''
    standing = classification(coursestaken) # to get total hours completed

    left = "Your degree plan summary:"
    right = "({} hours total)".format(standing[1])
    heading = "{:<30}{:>50}".format(left, right)
    line = '=' * 80
    
    print(line)
    print(heading)
    print(line)

    print()

    for c in degreeplan:
        # c[0] = term, c[1] = course number, c[2] = course title
        print("{:12} {:9} {}".format(c[0], c[1], c[2]))

    print(line)
    print(caveat)
    print()

def saveSummary(degreeplan, coursestaken):
    '''Save the degree plan summary to a file
       saveSummary(degreeplan : [(str, str, str)]) -> NoneType (+ desired side effects)
    '''
    # ask user if he/she wants to save degreeplan summary to a file
    print("If you want to save this summary to a file, enter a filename, ")
    filename = input("otherwise just press <Enter> to quit: ")
    print()

    # just return if user presses <Enter>
    if filename == '':
        return

    standing = classification(coursestaken) # to get total hours completed

    left = "Your degree plan summary:"
    right = "({} hours total)".format(standing[1])
    heading = "{:<30}{:>50}".format(left, right)
    line = '=' * 80
    
    # a file name was given; write to the file
    try:
        with open(filename, 'w') as file:
            file.write(line + '\n')
            file.write(heading + '\n')
            file.write(line + '\n')
            file.write('\n')

            for c in degreeplan:
                # c[0] = term, c[1] = course number, c[2] = course title
                file.write("{:12} {:9} {}\n".format(c[0], c[1], c[2]))
            file.write(line + '\n')
            file.write(caveat)
            file.write('\n\n')
            

        print("{} contains your degree plan summary!\n".format(filename))

    except:
        print("Couldn't write to the file!")
        # return without doing anything


def main():

    # print a welcome message
    print()
    print(welcome)
    
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

        # choose courses for the term; update degreeplan; mutates coursestaken!
        degreeplan = chooseCourses(term, choices, coursestaken, degreeplan)

        term = incTerm(term)

        print()

    # print the degree plan summary to the screen
    printSummary(degreeplan, coursestaken)

    # save the degree plan summary to a file if the user gives a file name
    saveSummary(degreeplan, coursestaken)

    # THE END


# this allows this program to be imported (without executing) into a unittest script for testing
if __name__ == "__main__":
    main()


# TODO:
#   print "the fine print" before the summary
#   redo testing worksheet because of several changes
#   (future) don't allow CSCI 4388 until the last semester

# Functions:
# reviewed tested isULC(course)
# reviewed tested prerequisites_met(course, coursestaken)
# reviewed tested LLCcomplete(coursestaken)
# reviewed tested getChoices(coursestaken)
# reviewed tested isCourseNumber(maybeCourseNumber)
# reviewed tested extractCourseNumbers(lines)
# reviewed tested add2CoursesTaken(course, coursestaken)
# reviewed tested getCoursesTaken()
# reviewed tested getTerm()
# reviewed tested incTerm(term)
# reviewed tested summerTerm(term)
# reviewed tested prereqFor(course, coursestaken)
# reviewed tested countHours(courses)
# reviewed tested classification(coursestaken)
# reviewed tested flipLabOrder(choices)
#                 displayChoices(term, choices, coursestaken)
#          tested checkCorequisites(courses)
#                 chooseCourses(term, courseMenu, degreeplan, coursestaken)
# reviewed tested printSummary(degreeplan)
# reviewed tested saveSummary(degreeplan, filename)
# reviewed tested main()
