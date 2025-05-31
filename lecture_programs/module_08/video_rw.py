# Files
# https://www.youtube.com/watch?v=nUumPCjn8UE

# Opening & Reading Files
# file = open("what-comes-next.txt", "r")  # "r" means read mode
# content = file.read()  # Reads the entire file as a string
# print(content)
# file.close()  # We must close the file explicitly

# Writing to a File
# file = open("example.txt", "w")  # Open in write mode
# file.write("Young & Happy")  # Overwrites file with this text
# file.close()  # Always close the file

# Appending new lines to a file
# file = open("example.txt", "a")  # Open in append mode
# file.write("\nAppending a new line.")  # Adds a line without erasing previous content
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# Writing practice
# file = open("practice.txt", "w")    # open in write mode
# file.write("This is my first practice file.")

# Appending practice
file = open("practice.txt", "a")    # open in append mode
file.write("\nThis is me appending the file.")
file = open("practice.txt", "r")
content = file.read()
print(content)
file.close()
