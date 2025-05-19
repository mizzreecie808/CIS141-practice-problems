# ChatGPT 🔥 Mini App 2:  Student Gradebook Tracker
# Track student names with their grades
# Let the user input each students name and grade
# Display the highest scorer's name, class average, and a full report
# Alice -> 92 (A), etc.
# grades = [88, 73, 95, 60, 45, 82, 77, 59, 99, 68]
students = int(input("How many students in the class? "))
names = []
grades = []
letter_grades = []

while len(grades) < students:
    student_input = input("Enter Student name and number grade: ")
    split_input = student_input.split(" ", 1)

    # input validation
    if len(split_input) !=2 or not split_input[1].isdigit():
        print("Invalid input. Please enter in the format: Name Grade")
        continue

    name = split_input[0]
    grade = int(split_input[1])

    # grade bounds checker
    if not 0 <= grade <= 100:
        print("Please enter a grade between 0 and 100.")
        continue

    if grade < 60:
        letter = "F"
    elif 60 <= grade <= 69:
        letter = "D"
    elif 70 <= grade <= 79:
        letter = "C"
    elif 80 <= grade <= 89:
        letter = "B"
    else:
        letter = "A"

    names.append(name)
    grades.append(grade)
    letter_grades.append(letter)

highest_index = grades.index(max(grades))
average_grade = sum(grades) / students

# Summary
print("---Class Grade Analyzer---")
print(f"Total students:\t{students}")
print(f"Highest grade:\t{names[highest_index]} → {grades[highest_index]}")
print(f"Average grade:\t{average_grade:.2f}")
print("Grade Summary")
for i in range(students):
    print(f"  {names[i]:<10} → {grades[i]:>3} ({letter_grades[i]})")


