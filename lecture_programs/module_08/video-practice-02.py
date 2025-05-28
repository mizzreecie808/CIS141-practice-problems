# Video - Problem solving text files
# Write a Python program that loads the orders.txt file into a dictionary.
# -Open file in read mode
# -Start a dictionary
# -Go through file line by line:
# -Add first value as key and second value as entry (\t in between values)
# -Close file

orders = {}

with open("orders.txt", "r") as file:
    for line in file:
#         split_line = line.strip().split("\t")
#         key = split_line[0]
#         val = split_line[1]
        key, val = line.strip().split("\t")
        orders[key] = val

print(orders)

