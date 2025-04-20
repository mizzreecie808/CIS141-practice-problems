# Reading - Numbers in Python
# Types - Integer, Floating Point or Real Number, Complex Number & Boolean
type_int = 5
type_float = 1.2
type_complex = 10j

# Common math functions
# print(abs(-12)) #12
# print(pow(2, 3)) #8
# print(round(17.3)) #17
# print(round(3.14159, 2)) #3.14
# print(min(12, 2, 44, 199)) #2
# print(max(12, 2, 44, 199)) #199

import math
# print(math.pi)
# print(math.e)
# print(math.ceil(3.621)) #4
# print(math.floor(3.621)) #3
# print(math.sqrt(225)) #15

# Formatting numbers
p = 18819.99   #principal
r = 0.05        #rate of interest
t = 2           #years

si = p * r * t
print("Simple interest at the end of 2 years $", format(si, "0.2f"))
print("Width Precision: ", format(si, "9.2f"))

print("Scientific Notation: ", format(5482.52291, "10.2E"))
