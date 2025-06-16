# Event-Driven Programming
import tkinter as tk

# 🪟 Create the main window
window = tk.Tk()

# Set the title of the window
window.title("One GUI to Rule Them All")

# Set the initial size of the window (width x height)
window.geometry("800x500")

# 🖼️ Creating Canvas for drawing & text
canvas = tk.Canvas(window, width=800, height=500, bg='white')
# .pack() makes the canvas show up in the window
canvas.pack()

# 🖱️ Prints location on canvas where user clicked
def on_canvas_click(event):
    print(f"Mouse clicked at ({event.x}, {event.y})")

# canvas.bind connects mouse clicks to on_canvas_click function
canvas.bind("<Button-1>", on_canvas_click)

# 🟪 Draw a rectangle on the canvas
# Purple rectangle: top-left corner (50, 50) bottom-right (100, 100)
rect = canvas.create_rectangle(50, 50, 100, 100, fill="purple", outline="")

# 🧲 Define what happens when dragging starts
# Runs on first click of the rectangle, saves mouse position in canvas.data
def start_drag(event):
    # Store the starting position
    canvas.data = {"x": event.x, "y": event.y}

# 🚚 Define what happens during dragging
# dx & dy are how far the mouse has moved
# canvas.move moves the rectangle by dx and dy amount
# canvas.data updates stored mouse position
def do_drag(event):
    dx = event.x - canvas.data["x"]
    dy = event.y - canvas.data["y"]
    canvas.move(rect, dx, dy)
    canvas.data = {"x": event.x, "y": event.y}

# ButtonPress-1 specifies pressing of the left mouse button, start_drag is the event that is triggered
canvas.tag_bind(rect, "<ButtonPress-1>", start_drag)
# B1-Motion specifies motion of the mouse after pressing the left mouse button
canvas.tag_bind(rect, "<B1-Motion>", do_drag)
