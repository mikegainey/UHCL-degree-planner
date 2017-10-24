# requirements is a dictionary; the key is a course rubric, 'PHYS 2325'
#   the value is a tuple, consisting of
#   - the full title of the course, 'University Physics I'
#   - a set of prerequisites, {'MATH 2413'}
requirements = {
    "WRIT 1301": ("Composition I", set()),
    "WRIT 1302": ("Composition II", set()),
    "MATH 2413": ("Calculus I", set()),
    "PHYS 2325": ("University Physics I and Lab (PHYS 2125)", set()),
    "PHYS 2326": ("University Physics II and Lab (PHYS 2126)", set()),
    "HIST 1301": ("U.S. History I", set()),
    "HIST 1302": ("U.S. History II", set()),
    "POLS 2305": ("Federal Government", set()),
    "POLS 2306": ("Texas Government", set()),
    "COMM 1315": ("Public Speaking", set()),
    "PSYC 1100": ("Learning Frameworks", set()),
        
    "MATH 2305": ("Discrete Math (LLC)", {"MATH 2413"}),
    "CSCI 1470": ("Computer Science I (LLC)", set()),
    "PHYS 2325": ("University Physics I (LLC)", {"MATH 2413"}),
    "CSCI 1471": ("Computer Science II (LLC)", {"CSCI 1470", "MATH 2413"}),
    "PHYS 2326": ("University Physics II (LLC)", {"MATH 2414", "PHYS 2325"}),
    "MATH 2318": ("Linear Algebra", {"MATH 2413"}),
    "CSCI 2315": ("Data Structures (LLC)", {"CSCI 1471"}),
    "CENG 3312": ("Digital Circuits & Lab", {"MATH 2414", "PHYS 2326"}),
    "CSCI 3352": ("Advanced Data Structures", {"CSCI 2315", "MATH 2305", "MATH 2414", "PHYS 2325", "PHYS 2326"}),
    "CSCI 3331": ("Computer Organization & Assembly Language", {"CSCI 2315", "MATH 2305", "MATH 2414", 
                                                                "PHYS 2325",  "PHYS 2326"}),
    "STAT 3334": ("Probability & Statistics ...", {"MATH 2413", "MATH 2414"}),
    "CENG 3331": ("Intro to Telecom and Neworks & Lab",  {"CENG 3312"}),
    "CSCI 4333": ("Design of Database Systems", {"CSCI 2315"}),
    "SWEN 4342": ("Software Engineering", {"CSCI 1470", "CSCI 2315"}),
    "CSCI 3321": ("Numerical Methods", {"MATH 2318", "MATH 2320", "CSCI 1471"}),
    "WRIT 3315": ("Technical Writing", set()),
    "CENG 3351": ("Computer Architecture & Lab (take with CSCI 4354)", {"CENG 3312"}),
    "CSCI 4354": ("Operating Systems (take with CENG 3351)", {"CSCI 2315", "CSCI 3331", "MATH 2305",
                                                              "MATH 2414", "PHYS 2325", "PHYS 2326"}),
    "CSCI 4388": ("Senior Project in Computer Science", {"CSCI 3352", "SWEN 4342"}),
    "CSCI 4320": ("(elective) Web Application Development", {"CSCI 2315"}),
    "CSCI 4350": ("(elective) Computer Graphics and Interface Design", {"MATH 2318",  "MATH 2413"}),
    "CSCI 4362": ("(elective) Computer Game Programming: Theory and Practice", {"CSCI 1470"}),
    "CSCI 4323": ("(elective) Computer Security", {"CSCI 1471"})
}


corereq = {'WRIT 1301', 'WRIT 1302', 'MATH 2413', 'PHYS 2325', 'PHYS 2326', 'HIST 1301', 'HIST 1302',
           'POLS 2305', 'POLS 2306', 'COMM 1315', 'PSYC 1100', 'PHYS 2125', 'PHYS 2126'}

majorreq = {'CHEM 1311', 'CHEM 1111', 'MATH 2305', 'MATH 2318', 'MATH 2414', 'MATH 2320', 'STAT 3334',
            'CSCI 1470', 'CSCI 1471', 'CSCI 3331', 'CSCI 2315', 'CSCI 3352', 'CSCI 4333', 'CSCI 3321',
            'CSCI 4354', 'CENG 3312', 'CENG 3331', 'CENG 3351', 'SWEN 4342', 'WRIT 3315', 'CSCI 4388'}

LLC = {'CSCI 1470', 'CSCI 1471', 'CSCI 2315', 'PHYS 2325', 'PHYS 2326', 'MATH 2413', 'MATH 2414', 'MATH 2305', 'WRIT 1301'}

