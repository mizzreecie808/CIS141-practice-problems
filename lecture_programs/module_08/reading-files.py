# Reading - File I/O
# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/File_IO
# file_object = open(filename, mode)

# Write a file
with open("test.txt", "wt") as out_file:
    out_file.write("This Text is going to out file\nLook at it and see!")

# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)




