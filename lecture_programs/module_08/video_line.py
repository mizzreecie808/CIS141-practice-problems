# with Statements & Processing Text Files with Loops
# https://www.youtube.com/watch?v=4k3To_oq9_c

# with keyword: a shortcut to file management
# manages file and automatically closes file
# with open("what-comes-next.txt", "r") as file:
#     print(file.read())

# processing line by line
# more manageable
line_num = 1
with open("what-comes-next.txt", "r") as file:
    for line in file:
        line_num_and_line = f"{str(line_num):<4} {line}"
#         line_num_and_line = str(line_num) + "\t" + line
        print(line_num_and_line, end="")
        line_num += 1
