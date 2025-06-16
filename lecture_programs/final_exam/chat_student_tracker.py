# ChatGPT - 🧩 Mini Final Challenge: Student Grades Tracker
# Ask user name
# If in students, calculate & print average grade rounded to 2 decimals
# Print pass if >= 60 else print
# If not in students print Student not found

students = {
    "Alice": [88, 92, 79],
    "Bob": [75, 84, 91],
    "Charlie": [100, 100, 100]
}

def grade_tracker(gradebook):
    # --- Ask student name ---
    user_input = input("What is your name? ")

    if user_input not in gradebook:
        return "Student not found."
    
    grades = gradebook[user_input]
    avg = round(sum(grades) / len(grades), 2)
    print(f"{user_input}'s average grade: {avg}")

    return "You passed!" if avg >= 60 else "Fail"

result = grade_tracker(students)
print(result)