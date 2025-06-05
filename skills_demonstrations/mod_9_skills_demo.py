# Mod 9 Skills Demonstration

import tkinter as tk
from tkinter import messagebox
import webbrowser

def get_gpa(score):
    #Errors out if the user puts in a value that can't be turned into a float
    try:
        score = float(score)
    except ValueError:
        return "Please enter a valid number."

    #Errors if the user puts in a number outside the specified range
    if score < 0 or score > 100:
        return "Score must be between 0 and 100."

    #Replace the code here with your code
    if score < 77:
        return "Sorry, you have to take the course again"
    else:
        return "Good job"

def submit_score():
    score = score_entry.get()
    result = get_gpa(score)
    result_label.config(text=result)

def open_link(event):
    webbrowser.open("https://www.olympic.edu/academics/academic-pathways/business-information-technology/computer-information-systems")

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
learn_label = tk.Label(window, text="Learn more")
learn_label.pack(pady=5)

# Hyperlink to the Olympic College Computer Information Systems homepage
link_label = tk.Label(window, text="Olympic College Computer Information Systems (CIS)", fg="blue", cursor="hand2")
link_label.pack(pady=5)
link_label.bind("<Button-1>", open_link)

window.mainloop()
