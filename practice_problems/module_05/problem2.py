# Problem #2
# Define a string variable (e.g., my_string = "Olympic College")
# Use a for loop to print each character on its own line
# Convert each character to uppercase before printing.

my_string = "Olympic College"

for letter in my_string:
    print(letter.upper())
print()


# additional practice, skip any spaces
for letter in my_string:
    if letter == " ":
        continue
    print(letter.upper())
print()
