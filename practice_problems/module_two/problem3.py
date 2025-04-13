'''
Create a program that:
Prompts for the side lengths of a triangle
Computes the area using Heron's formula.
Heron's formula
Area = Square root of√s(s - a)(s - b)(s - c) where
s = half the perimeter, or (a + b + c)/2.
'''
import math

a, b, c = float(input("Length of side a?")), float(input("Length of side b?")), float(input("Length of side c?"))

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("s = ", s)
print("area = ", area)
