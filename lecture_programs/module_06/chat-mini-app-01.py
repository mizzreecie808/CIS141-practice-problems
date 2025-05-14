# ChatGPT 🧩 Mini App 1: Class Grade Analyzer
# Ask the user how many grades they want to enter
# Collect the grades in a list
# Analyze the grades (highest, lowest, average, letter grades, failing grades)
# Display a full summary
# Ask if they want to analyze another batch

# grades = [88, 73, 95, 60, 45, 82, 77, 59, 99, 68]
students = int(input("How many grades do you want to analyze? "))
grades = []
failing_list = []
letter_grades = []
failing = 0

while len(grades) < students:
    grade_input = input("Grade:\t")
    if not grade_input.isdigit():
        print("Please enter a valid grade between 0 and 100.")
        continue

    grade = int(grade_input)
    if not 0 <= grade <= 100:
        print("Please enter a valid grade between 0 and 100.")
        continue

    # Safe to process
    grades.append(grade)

    if grade < 60:
        failing_list.append(grade)
        letter_grades.append("F")
        failing += 1
    elif 60 <= grade <= 69:
        letter_grades.append("D")
    elif 70 <= grade <= 79:
        letter_grades.append("C")
    elif 80 <= grade <= 89:
        letter_grades.append("B")
    else:
        letter_grades.append("A")


highest = max(grades)
lowest = min(grades)
average_grade = sum(grades) / students
failing_list.sort()

# Summary
print("---Class Grade Analyzer---")
print(f"Total students:\t{students}")
print("Grade Summary")
for i in range(len(grades)):
    print(f"   {grades[i]} → {letter_grades[i]}")
print(f"Highest grade:\t{highest}")
print(f"Lowest grade:\t{lowest}")
print(f"Average grade:\t{average_grade:.2f}")
print(f"Grades >= 60:\t{students - failing}")
print(f"Failing grades:\t{failing_list}")
