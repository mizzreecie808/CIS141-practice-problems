# Reading - Count to 10, While Loops
# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Count_to_10

a = 0
while a < 10:
    a += 1
    print(a)

# Fibonacci sequence
a = 0
b = 1
count = 0
max_count = 20

while count < max_count:
    count += 1
    print(a, end = " ") # this keeps from creating a new line
    old_a = a           # we need to keep track of "a" since we change it
    a = b
    b += old_a
print() # adds empty new line
