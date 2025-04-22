# Reading - Numbers in Python
# Types - Integer, Floating Point or Real Number, Complex Number & Boolean
type_int = 5
type_float = 1.2
type_complex = 10j

# Common math functions
print("Absolute:", abs(-12)) #12
print("Exponent:", pow(2, 3)) #8
print("Round Whole #:", round(17.3)) #17
print("Round 2 Digit:", round(3.14159, 2)) #3.14
print("Minimum Value:", min(12, 2, 44, 199)) #2
print("Maximum Value:", max(12, 2, 44, 199)) #199

import math
print("Pi:", math.pi)
print("e:", math.e)
print("Ceil:", math.ceil(3.621)) #4
print("Floor:", math.floor(3.621)) #3
print("Absolute in Float:", math.fabs(2)) #2.0
print("Sqrt:", math.sqrt(225)) #15
print("Log:", math.log(2)) #0.6931471805599453

# Formatting numbers
p = 18819.99   #principal
r = 0.05        #rate of interest
t = 2           #years

si = p * r * t
print(f"Simple interest at the end of 2 years ${si:0.2f}")
print(f"Width Precision: {si:9.2f}")
print("Scientific Notation:", format(5482.52291, "10.2e"))
print("With comas:", format(98813343817.7129, "5,.2f"))
print(f"With percentage: {0.71981:%}")
print(f"With percentage: {52:%}")

# Alignment
print(f"{math.pi:<10.2f} <<10 trailing spaces") # output the value left justfied
print(f"{95:5d} <<5 leading spaces")

#F For
print(f"{4:b} <<binary equivalent of decimal 4")
print(f"{255:x} <<hexadecimal equivalent of 255")
print(f"{9:o} <<octal equivalent of decimal 9")
print(f"{100:<10d} <<Left align with total 10 width")

