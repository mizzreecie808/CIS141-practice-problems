# ChatGPT - 🧪 Challenge: GPA Analyzer
gpas = {
    "Alice": [3.5, 3.9, 4.0],
    "Bob": [2.8, 3.2, 3.0],
    "Charlie": [1.8, 2.0, 1.9]
}

def analyze_gpas(gpas):
    # Loop through each student
    student_letter= {}

    for name, grades in gpas.items():
        # Calculate average GPA for each student
        avg = sum(grades) / len(grades)

        # Stores results in new dictionary { "Student": "Letter Grade" }
        if avg >= 3.7:
            student_letter[name] = "A"
        elif avg >= 3.0:
            student_letter[name] = "B"
        elif avg >= 2.0:
            student_letter[name] = "C"
        else:
            student_letter[name] = "F"

    print(student_letter)
    return student_letter

assert analyze_gpas(gpas) == {'Alice': 'A', 'Bob': 'B', 'Charlie': 'F'}
print("Test passed")

phrase = "Python"

for char_code in phrase:
    print(f"Letter: {char_code}")