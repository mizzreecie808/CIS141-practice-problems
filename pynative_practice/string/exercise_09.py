# https://pynative.com/python-string-exercise/
# Exercise 9: Calculate the sum and average of the digits present in string
s1 = "PYnative29@#8496"

# initiate sum
sum = 0
count = 0

for char in s1:
    if char.isdigit():
        count += 1
        sum += int(char)

print(f"Sum is: {sum}")
print(f"Average is: {sum / count}")
