# UHCL-degree-planner

## Purpose
This program will help UHCL Computer Science B.S. students select courses for the next term and all subsequent terms until graduation.

## Product Features
- Students will be presented with a list of only the courses eligible to be taken for each term.  Courses that have unmet prerequisites will not be shown.  Upper-Level CSCI and CENG courses will not be shown until the CS Lower-Level Core is completed. 
- For each course that can be taken, the number of other courses for which that course is a prerequisite will be shown.  This should encourage students to prioritize taking courses that are prerequisites of other courses.
- At the beginning of the program, students can indicate courses already completed at the keyboard and/or from an input file.
- After choosing courses for each term until all requirements are completed, students will be presented with a degree plan summary that can also be saved to a file.

## Details
- The program file to run is `UHCLdegreeplanner.py`.  It was developed using Python 3.6.3 on a computer running Ubuntu 17.10 GNU/Linux but doesn't contain any platform-specific code.
- See `test_input.txt` or `mikesinput.txt` for examples of files containing completed courses to add.
- See `test_output.txt` for an example of a degree plan summary.
- This program uses requirements found in the UHCL 2017-2018 undergraduate catalog.
- [Undergraduate Catalog 2017-2018, Computer Science B.S. Degree Requirements](https://catalog.uhcl.edu/current/undergraduate/degrees-and-programs/bachelors/computer-science-bs)
- [The 2-page 2017-2018 CS BS degree plan](https://www.uhcl.edu/academics/degrees/documents/cse/wbs-computerscience.pdf)
- [A 4-year CS BS degree map from www.uhcl.edu](https://www.uhcl.edu/academics/degrees/documents/cse/maps/wbs-computerscience.pdf)

## User Instructions
If you are a UHCL Computer Science B.S. student, this program will help you
choose courses to take next term and each successive term until graduation.

First, tell the program the courses you have already completed.  You can enter
them one-at-a-time at the keyboard and/or you can enter a file name with a list
of courses.

In the file, list course numbers (like CSCI 1470) one-per-line.  Anything on the
line after the course number will be ignored so you can include notes after
course numbers or on separate lines.

After entering your starting term, you will see a menu of courses that you are
eligible to take.  Choose courses for the term by menu number.  The program will
then restate your choices and ask you to verify them before moving to the next
term.

Next to many courses in the list, there will be something that looks like
"(prereq for # courses)."  It shows that the listed course is a prerequisite for
the given number of other courses.  Since you can't take those other courses
until this course is completed, its a good idea to prioritize taking courses
that are prerequisites for others.  Calculus I is a good example.  You should
also prioritize courses in the Lower-Level Core since upper-level CSCI and CENG
courses can't be taken until the LLC is complete.

After you have chosen all of your courses, the program will display your
complete degree plan summary.  If you enter a file name, the summary will be
saved as a text file in the same folder as the program.

## Caveat
This program uses course information and degree requirements from the
UHCL 2017-2018 undergraduate catalog.  Refer to your personal CPS for the
requirements that apply to you.