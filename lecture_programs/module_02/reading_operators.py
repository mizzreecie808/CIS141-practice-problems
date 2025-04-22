# Reading - Operators in Python
# Operators & Expressions

# Arithmetic Operators
# print("Addition: 2 + 2 =", 2 + 2)
# print("Subtraction: 4 - 2 = ", 4 - 2)
# print("Multiplication: 4 * 2 =", 4 * 2)
# print("Float Division: 5 / 2 =", 5 / 2, "<< Returns a floating point result")
# print("Integer Division: 5 // 2 =", 5 // 2, "<< Returns an integer")
# print("Float Division: -5 / 2 =", -5 / 2, "<< Returns a floating point result")
# print("Integer Division: -5 // 2 =", -5 // 2, "<< Returns an integer")
# print("Exponetiation: 5 ** 3 =", 5 ** 3)
# print("Remainder: 10 % 3 =", 10 % 3, "<< Common use to determine even number")

# Operator Precedence & Associativity
# ** right to left then
# *, /, //, % left to right
# then +, - left to right
# print("10 * 5 + 9 =", 10 * 5 + 9)
# print("9 + 5 * 10 =", 9 + 5 * 10)
# print("5 + 12 / 2 * 4 =", 5 + 12 / 2 * 4)
# print("5 + 12 / (2 * 4) =", 5 + 12 / (2 * 4))

# Compound Assignment Operator
# x = 10
# x += 5 # <<-- same thing x = x + 5
# print("x =", x)

# Type Conversion
# print("Integers: 45 * 3 =", 45 * 3)
# print("Floats: 3.4 * 5.3 =", 3.4 * 5.3)
# print("Float & Integer: 4 * 5.2 =", 4 * 5.2)
# print("Convert Float to Integer: int(2.7) =", int(2.7))
# print("Convert Integer to Float: float(2) =", float(2))
# print("Convert Float to String: str(2.7) =", str(2.7))

# Breaking Statements into Multiple Lines using \
# result = 1111100 + 45 - (88 / 43) + 783 \
#     + 10 - 33 * 1000 + 88 + 3772
# print("This is the result of the above \
# statement", result)

# Bool Type
# print(type(True))
# print(int(True))
# print(int(False))
# print("Truthy or Falsy? bool(""):", bool(""))
# print("Truthy or Falsy? bool(12):", bool(12))
# print("Truthy or Falsy? bool(0):", bool(0))

# Relational Operators
# print("3 < 4 =", 3 < 4)
# print("90 > 450 =", 90 > 450)
# print("10 <= 11 =", 10 <= 11)
# print("31 >= 40 =", 31 >= 40)
# print("100 != 101 =", 100 != 101)
# print("50 == 50 =", 50 == 50)

# Logical Operators
# Used to combine two or more boolean expressions
# Precedence: >, >=, <, <=, == and !=
# AND operand returns TRUE if BOTH operands are TRUE, else returns FALSE
print("10 > 3 =", 10 > 3, "15 > 6 =", 15 > 6)
print("10 > 3 and 15 > 6 =", 10 > 3 and 15 > 6)
print("1 == 1 =", 1 ==1, "2 != 2 =", 2 != 2)
print("1 == 1 and 2 != 2 =", 1 == 1 and 2 != 2)

# OR operand returns FALSE when BOTH operands are FALSE, else returns TRUE
# OR operand is less than AND
print("100 < 200 or 55 < 6 =", 100 < 200 or 55 < 6)

# NOT operand negates the value of the expression
# NOT is higher than AND as well as OR
print("not 200 == 200 =", not 200 == 200)
print("not 10 <= 5 =", not 10 <= 5)

