'''
Module #2 Problem #2
Create a program that:
Prompts for 2 numbers
Outputs the +, -, *, and / of the first number by the second number.
'''

num_one = float(input("Enter first number: "))
num_two = float(input("Enter second number: "))

add = num_one + num_two
sub = num_one - num_two
mult = num_one * num_two
div = num_one / num_two

print("addition:", add)
print("subtraction:", sub)
print("multiplication:", mult)
print("division:", div)
