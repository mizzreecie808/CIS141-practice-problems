# ChatGPT 🎯 Mini Challenge 2: Class Grade Analyzer
# Print all the grades
# Calculates and prints: Highest, Lowest, Average, Index of highest
# How many students (grade >= 60)
# Prints list of failing grades <60
# 🌀 Twist: Add Letter Grades

grades = [88, 73, 95, 60, 45, 82, 77, 59, 99, 68]
highest = max(grades)
lowest = min(grades)
average_grade = sum(grades) / len(grades)
highest_index = grades.index(highest)
failing_list = []
over60 = len(grades)
letter_grades = []

for grade in grades:
    if grade < 60:
        failing_list.append(grade)
        letter_grades.append("F")
        over60 -= 1
    elif 60 <= grade <= 69:
        letter_grades.append("D")
    elif 70 <= grade <= 79:
        letter_grades.append("C")
    elif 80 <= grade <= 89:
        letter_grades.append("B")
    else:
        letter_grades.append("A")
failing_list.sort()

# Summary
print("---Class Grade Analyzer---")
print(f"Total students:\t{len(grades)}")
print("Grade Summary")
for i in range(len(grades)):
    print(f"   {grades[i]} → {letter_grades[i]}")
print(f"Highest grade:\t{highest}")
print(f"Lowest grade:\t{lowest}")
print(f"Average grade:\t{average_grade:.2f}")
print(f"Index of highest:\t{highest_index}")
print(f"Grades >= 60:\t{over60}")
print(f"Failing grades:\t{failing_list}")
