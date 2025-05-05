# Problem 2: Critical Hit?
# As user for a d20 roll (1-20)
# "Critical Hit!" when roll is 20
# "Critical Miss!" when roll is 1
# "Normal attack." otherwise
# can import random library to generate 1-20 roll

import random
roll = random.randint(1, 20)
print(roll)

if 2 <= roll <= 19:
	print("Normal attack")
elif roll == 20:
	print("Critical Hit!")
else:
	print("Critical Miss!")
