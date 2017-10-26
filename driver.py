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


coursestaken = set()

courseSet2 = {'WRIT 1302'}

course = 'WRIT 1301'

# given a course, return the number of courses that that course will unlock
def unlocks(course, courseSet2, coursestaken):
    count = 0
    for c in courseSet2:
        remainingPrerequisites = coursecatalog[c][1] - coursestaken
        a = course in remainingPrerequisites
        b = len(remainingPrerequisites) == 1
        if a and b:
            count += 1
    return count

u = unlocks(course, courseSet2, coursestaken)
print(u)
