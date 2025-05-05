# Module 04 Skills Demonstration
# Before Recording:
# Write a program that takes a student's grade (e.g. 91)
# and uses an if-elif-else statement to tell them the grade point average
# they'd receive in this class.
# Use the grading table in the Syllabus to complete this problem.

# students grade
student1 = 98  #GPA: 4.0 A
student2 = 84  #GPA: 2.7 B-
student3 = 71  #GPA: 1.3 D+

grade = 60

# grade point average using if-elif-else
if 96 <= grade:
    print("GPA: 4.0 A")
elif 93 <= grade < 96:
    print("GPA: 3.7 A-")
elif 90 <= grade < 93:
    print("GPA: 3.3 B+")
elif 87 <= grade < 90:
    print("GPA: 3.0 B")
elif 83 <= grade < 87:
    print("GPA: 2.7 B-")
elif 80 <= grade < 83:
    print("GPA: 2.3 C+")
elif 77 <= grade < 80:
    print("GPA: 2.0 C")
elif 73 <= grade < 77:
    print("GPA: 1.7 C-")
elif 70 <= grade < 73:
    print("GPA: 1.3 D+")
elif 67 <= grade < 70:
    print("GPA: 1.0 D")
elif 63 <= grade < 67:
    print("GPA: 0.7 D-")
else:
    print("GPA: 0.0 F")
