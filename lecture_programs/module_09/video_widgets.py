import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("One GUI to Rule Them All")
window.geometry("800x500")  # width x height

# Buttons
def on_button_click():
    print("Button was clicked")

btn = tk.Button(window, text="Click Me", command=on_button_click)
btn.pack(pady=10)   #padding around button

#Checkboxes
chk_state = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="I like Pokemon", var=chk_state)
checkbox.pack()

#Input Boxes
entry = tk.Entry(window)
entry.pack(pady=10)

#Images - use png
img = tk.PhotoImage(file="bulbasaur.png")
label_img = tk.Label(window, image=img)
label_img.pack()

#Menus
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

#Alerts
from tkinter import messagebox
messagebox.showinfo("Alert", "I want to be the very best!")

#Hyperlinks
def open_link(event):
    import webbrowser
    webbrowser.open("https://www.pokemon.com/us")

link = tk.Label(window, text="Visit Pokemon.com", fg="blue", cursor="hand1")
link.pack()
link.bind("<Button-1>", open_link)

