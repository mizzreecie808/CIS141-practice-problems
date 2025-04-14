'''
Module #2 Problem #3
Create a program that:
Prompts for the side lengths of a triangle
Computes the area using Heron's formula:
Area = Square root of√s(s - a)(s - b)(s - c) where
s = half the perimeter, or (a + b + c)/2
'''

# must import the math suite to use the square root function
import math

# practice assigned values simultaneously in a single line
a, b, c = float(input("Length of side a?")), float(input("Length of side b?")), float(input("Length of side c?"))

# first solve for "s"
s = (a + b + c) / 2

# second, using "s" solve for area
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("s = ", s)
print("area = ", area)
