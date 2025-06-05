import tkinter as tk
from tkinter import messagebox

# get function to "get" user input from the entry block
def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
        else:
            result = num1 / num2
            result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x300")

# Entry fields for number input
entry1 = tk.Entry(window, width=10)
entry1.pack(pady=5)
entry2 = tk.Entry(window, width=10)
entry2.pack(pady=5)

# Frame to hold the operation buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Operation buttons
add_button = tk.Button(button_frame, text="Add", command=add)
add_button.grid(row=0, column=0, padx=5)
subtract_button = tk.Button(button_frame, text="Subtract", command=subtract)
subtract_button.grid(row=0, column=1, padx=5)
multiply_button = tk.Button(button_frame, text="Multiply", command=multiply)
multiply_button.grid(row=0, column=2, padx=5)
divide_button = tk.Button(button_frame, text="Divide", command=divide)
divide_button.grid(row=0, column=3, padx=5)

# Label to display the result
result_label = tk.Label(window, text="Result:", font=("Arial", 20))
result_label.pack(pady=10)

window.mainloop()
