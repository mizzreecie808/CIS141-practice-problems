# Module 03 Skills Demonstration
str = "Code never lies, comments sometimes do"

# Calculate the length of the string & display it
length = len(str)
# print(length)

# Add a new line after the comma & display it
str1 = "Code never lies,\ncomments sometimes do"
# print(str1)

# Make every character in the string uppercase & display it
# print(str.upper())

# Use slicing to grab just "Code never lies" out of the string 15
sub_string = str[:15]

# Calculate the length of the above substring
length_sub = len(sub_string)

# Concatenate the length onto the end of the substring
display = f"{sub_string}: {length_sub}"

# Display it
print(display)
