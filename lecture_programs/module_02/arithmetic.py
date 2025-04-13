#Operator Precedence: Close to PEMDAS
#parentheses > exponent > multiplication/division/floor division/modulus > addition/subtraction
#result = 2**(4/2)
#print(result)

print("Addition: 2 + 2 =", 2 + 2)
print("Subtraction: 2 - 2 =", 2 - 2)
print("Multiplication: 2 * 2 =", 2 * 2)
print("Divison: 14 / 4 =", 14 / 4)
print("Floor Division: 14 // 4 =", 14 // 4)
print("Modulus (Remainder): 14 % 4 =", 14 % 4)
print("Exponentiation: 4 ** 4 =", 4 ** 4)

#Using same variable on both sides of assignment; augmented assignment
x = 6
print("x = ", x)
x = x + 2
print("x = ", x)
x += 2
print("x = ", x)

# What types are returned from these operators?
print(int(5 / 2))
print(5 // 2)
