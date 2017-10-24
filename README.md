# UHCL-degree-planner
My personal degee planner (course selection helper).

This is in the beginning stages of a re-factor to generalize the program to be helpful to any undergraduate CS student at UHCL and also to test the correctness of the internal functions.

The data consists of:
- requirements (change name to coursecatalog): A dictionary where keys are course rubrics (CSCI 1471).  Values are a tuple consisting of a long description string and a set of prerequisite courses (rubric list)

- corereq - a list of University Core requirements

- majorreq - a list of CS major requirements

- LLC - the CS Lower Level Core that needs to be complete before taking upper-level (3000- and 4000-level CSCI and CENG courses).

- 
