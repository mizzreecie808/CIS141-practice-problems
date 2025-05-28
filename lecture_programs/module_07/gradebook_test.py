# ChatGPT 🧩 Mini App 1: Student Gradebook Tracker - Tester
# gradebook_test.py

import gradebook_app

# Sample gradebook dictionary for testing
test_data = {
    "Alice": 92,
    "Diana": 98,
    "Fiona": 88,
    "Bob": 76,
    "Charlie": 85,
    "Ethan": 67,
    "George": 98
}

gradebook_app.display_students(test_data)
gradebook_app.calculate_average(test_data)
gradebook_app.get_top_student(test_data)
