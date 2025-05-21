# ChatGPT 🧩 Mini App 1: Student Gradebook Tracker
# Enter names and grades for multiple students
# Store them in a dictionary
# Use functions to add a student, calculate average
# Show all students and their grades, find top-scoring students

gradebook = {}

# Ask user for student name and grade, then add to dict
def add_student(gradebook):
    user_input = input("Student name and grade (Alice, 95): ")

    # Split input into 2 parts, name and grade
    input_parts = user_input.split(",")
    name = input_parts[0].strip().capitalize()
    grade = int(input_parts[1].strip())

    # Update gradebook
    gradebook.update({name: grade})

    # For debugging
    print(gradebook)

# def calculate_average(gradebook):
    # Return the average of all grades

# def display_students(gradebook):
    # Print each student and their grade

# def get_top_student(gradebook):
    # Find and return student(s) with highest grade

add_student(gradebook)
