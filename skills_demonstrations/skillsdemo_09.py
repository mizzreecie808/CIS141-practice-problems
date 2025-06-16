# Module 09 Skills Demonstration
# students grade
student1 = 100.5  #GPA: 4.0 A
student2 = 82.5  #GPA: 2.7 B-
student3 = 71  #GPA: 1.3 D+

grade_lookup = {
    (96, 100): (4.0, "A", "Excellent work! 🎉"),
    (93,  96): (3.7, "A-", "Excellent work! 🎉"),
    (90,  93): (3.3, "B+", "Great job! 👍"),
    (87,  90): (3.0, "B", "Great job! 👍"),
    (83,  87): (2.7, "B-", "Great job! 👍"),
    (80,  83): (2.3, "C+", "Good effort. Keep pushing! 💪"),
    (77,  80): (2.0, "C", "Good effort. Keep pushing! 💪"),
    (73,  77): (1.7, "C-", "Good effort. Keep pushing! 💪"),
    (70,  73): (1.3, "D+", "You're getting there. Review the material. 📘"),
    (67,  70): (1.0, "D", "You're getting there. Review the material. 📘"),
    (63,  67): (0.7, "D-", "You're getting there. Review the material. 📘"),
    (0,   63): (0.0, "F", "Don't give up! Seek help and try again. 🚀"),
}

def get_gpa(score):
    #Errors out if the user puts in a value that can't be turned into a float
    try:
        score = float(score)
    except ValueError:
        return "Please enter a valid number."

    #Errors if the user puts in a number outside the specified range
    if score < 0 or score > 100:
        return "Score must be between 0 and 100."

    for (low, high), (gpa, letter, message) in grade_lookup.items():
        if low <= score < high:
            return f"You got an {letter}, {message}"

get_gpa(student1)
get_gpa(student2)
get_gpa(student3)
