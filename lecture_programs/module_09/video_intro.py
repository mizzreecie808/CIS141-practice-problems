import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("One GUI to Rule Them All")
window.geometry("800x500")  # width x height

# Creating Canvas for drawing & text
canvas = tk.Canvas(window, width=800, height=500, bg='white')
canvas.pack()

# Draw a rectangle onto Canvas
canvas.create_rectangle(50, 50, 150, 150, fill="blue", outline ="purple")
# Draw a circle (oval) onto Canvas
canvas.create_oval(200, 50, 300, 150, fill="red", outline ="black")

# Draw text onto Canvas
canvas.create_text(200, 250, text="Hello, GUI World!", font=("Arial", 16))

# Run the event loop
window.mainloop()
