# Boolean Operators & Truth Tables
# https://www.youtube.com/watch?v=oPL9I9X6lY8
# AND, OR, NOT are the most common boolean
# AND Operator (&)
#  A     B     A & B
#--------------------
# True  True   True
# True  False  False
# False True   False
# False False  False

print("True and True =\t", True and True)
print("True and False =\t", True and False)

# OR Operator (||)
#  A     B     A & B
#--------------------
# True  True   True
# True  False  True
# False True   True
# False False  False

print("True or False =\t", True or False)
print("False or False =\t", False or False)

# NOT Operator (||)
# Toggles true --> false or false --> true
#  A    NOT A
#--------------------
# True  False
# False True

# XOR Operator
# Checks if the 2 operands are the same
#  A     B     A & B
#--------------------
# True  True   False
# True  False  True
# False True   True
# False False  False

print("True ^ False =\t", True ^ False)
