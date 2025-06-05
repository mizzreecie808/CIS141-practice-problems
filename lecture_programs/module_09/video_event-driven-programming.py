# Event-Driven Programming
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("One GUI to Rule Them All")
window.geometry("800x500")  # width x height

# Creating Canvas for drawing & text
canvas = tk.Canvas(window, width=800, height=500, bg='white')
canvas.pack()

'''
# Prints location on canvas where user clicked
def on_canvas_click(event):
    print(f"Mouse clicked at ({event.x}, {event.y})")

canvas.bind("<Button-1>", on_canvas_click)
'''
# Initial coordinates for a shape
rect = canvas.create_rectangle(50, 50, 100, 100, fill="purple")

def start_drag(event):
    # Store the starting position
    canvas.data = {"x": event.x, "y": event.y}

def do_drag(event):
    dx = event.x - canvas.data["x"]
    dy = event.y - canvas.data["y"]
    canvas.move(rect, dx, dy)
    canvas.data = {"x": event.x, "y": event.y}

canvas.tag_bind(rect, "<ButtonPress-1>", start_drag)
canvas.tag_bind(rect, "<B1-Motion>", do_drag)
