# Module 05 Skills Demonstration
# Before Recording:
# Use a loop (for or while) to go through numbers from 1 to 20.
# If a number is a multiple of 3, use continue to skip printing it. modulus
# Otherwise, print the number.

num = 0

while num < 20:
    num += 1
    if num % 3 == 0:
        print(f"{num} is a multiple of 3")
        continue
    print(num)
print("Exited While Loop")


# Explain your code at a high-level
# Test your code to demonstrate that it is functional.
# Explain how the loop your wrote works, as if you were explaining it
# to a student who was learning about this for the first time.
# Discuss what is happening in your program for at least 4 iterations of the loop.
