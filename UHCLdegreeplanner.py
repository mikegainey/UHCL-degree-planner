# coursecatalog is a dictionary; the key is a course rubric, 'PHYS 2325'
#   the value is a tuple, consisting of
#   - the full title of the course, 'University Physics I'
#   - a set of prerequisites, {'MATH 2413'}

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
