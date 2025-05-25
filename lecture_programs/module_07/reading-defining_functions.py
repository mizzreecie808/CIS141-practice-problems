# Reading - Defining Functions
# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Defining_Functions
# Functions repeat tasks
# Variables in a function don"t override global variables

def print_welcome(name):
    print("Hello!")
    print("Welcome,", name)

def area_type(shape):
    if shape.strip().lower() == "rect":
        print("Enter the width and height below.")
        w = positive_input("Width: ")
        h = positive_input("Height: ")
        area = w * h
        print(f"Width = {w} Height = {h} so Area = {area}")
        return area
    else:
        print("enter the radius of the circle.")
        r = positive_input("Radius: ")
        area = 3.14 * r**2
        print(f"Radius = {r} so Area = {area}")
        return area

def positive_input(prompt):
    number = float(input(prompt))
    while number <= 0:
        print("Must be a positive number")
        number = float(input(prompt))
    return number

user_name = input("Your Name: ")
print_welcome(user_name)

user_shape = input("Would you like to find the area of a rectangle or circle? (Type rect/circ) ")
area_type(user_shape)
