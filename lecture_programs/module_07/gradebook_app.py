# ChatGPT 🧩 Mini App 1: Student Gradebook Tracker
# gradebook_app.py

# Ask user for student name and grade, then add to dict
def add_student(gradebook):
    print("Type 'quit' to exit")

    while True:
        user_input = input("Student name and grade (Alice, 95): ")

        if user_input.lower().strip() == "quit":
            print("Exiting Program.")
            print(gradebook)
            return

        # Split input into 2 parts, name and grade
        input_parts = user_input.split(",")

        if len(input_parts) != 2:
            print("❌ Please enter data in the format: Name, Grade")
            continue

        name = input_parts[0].strip().capitalize()
        if name in gradebook:
            print(f"⚠️ {name} already exists. Overwriting grade.")


        try:
            grade = int(input_parts[1].strip())
        except ValueError:
            print("❌ Grade must be a number.")
            continue

        # Update gradebook
        gradebook[name] = grade

        # For debugging
        print(f"✅ Added {name} with grade {grade}.")

# Ask user for student name, then remove from dict
def remove_student(gradebook):
    print("Type 'quit' to exit")

    while True:
        user_input = input("Enter student name to delete: ")

        if user_input.lower().strip() == "quit":
            print("Exiting Program.")
            return

        name = user_input.capitalize().strip()
        if not name in gradebook:
            print(f"⚠️ {name} not in gradebook.")
            continue

        # Remove student from gradebook
        gradebook.pop(name)

        # For debugging
        print(f"✅ Removed {name}.")

# Return the average of all grades
def calculate_average(gradebook):

    if not gradebook:
        print("📭 No students to average.")
        return

    total = sum(gradebook.values())
    avg = total / len(gradebook)

    print(f"🧮 Average Grade: {round(avg, 2)}")
    return round(avg, 2)

# Print each student and their grade
def display_students(gradebook):
    if not gradebook:
        print("📭 Gradebook is empty.")
        return

    else:
        print(f"{'--📋 Student Grades 📋--':^21}")
        # .items() returns both the key and the value
        for name in sorted(gradebook):
            print(f"   {name:<15}{gradebook[name]:>4}")
    print(f"🧮 Total students: {len(gradebook)}")

# Find and return student(s) with highest grade
def get_top_student(gradebook):

    if not gradebook:
        print("📭 Gradebook is empty.")
        return

    top_students = []
    highest = max(gradebook.values())

    for name, grade in gradebook.items():
        if grade == highest:
            top_students.append((name, grade))

    # Keep data and display logic separate
    for name, grade in top_students:
        print(f"🧠 Highest Grade: {name:<15}{grade:>3}")

    return top_students

# Only runs if this file is run directly, not when imported
if __name__ == "__main__":
    # Optional: local test or demo
    demo_data = {
        "Alice": 92,
        "Diana": 98,
        "Fiona": 88,
        "Bob": 76,
        "Charlie": 85,
        "Ethan": 67,
        "George": 98
    }
    display_students(demo_data)
    get_top_student(demo_data)
