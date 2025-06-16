# Mod 9 Skills Demonstration

import tkinter as tk
from tkinter import messagebox
import webbrowser

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
    # Errors out if the user puts in a value that can't be turned into a float
    try:
        score = float(score)
    except ValueError:
        return "Please enter a valid number."

    # Errors if the user puts in a number outside the specified range
    if score < 0 or score > 100:
        return "Score must be between 0 and 100."

    # Enter your code here
    for (low, high), (gpa, letter, message) in grade_lookup.items():
        if low <= score < high:
            return f"You got a {gpa}: {letter}.\n{message}"

def submit_score():
    score = score_entry.get()
    result = get_gpa(score)
    result_label.config(text=result)

def open_link(event):
    webbrowser.open("https://www.olympic.edu/academics/academic-pathways/business-information-technology/computer-information-systems")

def open_learn(event):
    webbrowser.open("https://mindthegraph.com/blog/what-is-a-gpa/")


# Create the main window
window = tk.Tk()
window.title("Course GPA Evaluator")
window.geometry("500x400")

# Set up the menu with an Exit option
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

# Display the logo image at the top
logo_img = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(window, image=logo_img)
logo_label.pack(pady=10)

# Label and entry for score input
info_label = tk.Label(window, text="This app helps you determine your course GPA(0.0-4.0) from your class score (0-100):")
info_label.pack(pady=5)
score_label = tk.Label(window, text="Enter your score (0-100):")
score_label.pack(pady=5)
score_entry = tk.Entry(window)
score_entry.pack(pady=5)

# Button to submit the score
submit_button = tk.Button(window, text="Submit", command=submit_score)
submit_button.pack(pady=10)

# Label to display the GPA message/result
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

#Learn more text
learn_label = tk.Label(window, text="Learn more", fg="blue", cursor="hand2")
learn_label.pack(pady=5)
# Added
learn_label.bind("<Button-1>", open_learn)

# Hyperlink to the Olympic College Computer Information Systems homepage
link_label = tk.Label(window, text="Olympic College Computer Information Systems (CIS)", fg="blue", cursor="hand2")
link_label.pack(pady=5)
link_label.bind("<Button-1>", open_link)

window.mainloop()
