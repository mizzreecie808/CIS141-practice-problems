# Module 03 Skills Demonstration
str = "Code never lies, comments sometimes do"

# Calculate the length of the string & display it
length = len(str)
print(length)

# Add a new line after the comma & display it
# Find comma and use index # to slice string
comma = str.find(",") + 1
str1 = str[:comma] + "\n" + str[comma + 1:]
print(str1)

# Make every character in the string uppercase & display it
print(str.upper())

# Use slicing to grab just "Code never lies" out of the string
# Find comma and use index # to get sub-string
comma = str.find(",")
sub_string = str[:comma]
print(sub_string)

# Calculate the length of the above substring
# Concatenate the length onto the end of the substring
# Display it
length = len(sub_string)
print(sub_string, length)
