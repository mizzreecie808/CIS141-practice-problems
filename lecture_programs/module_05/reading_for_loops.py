# Reading - For Loops
# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/For_Loops

one_to_ten = range(1, 11)
for count in one_to_ten:
    print(count, end= " ")
print()

for count in range(1, 11):
    print(count, end = " ")
print()

demolist = ["life", 42, "the universe", 6, "and", 7, "everything"]
for item in demolist:
    print(f"The current item is: {item}")

list = [2, 4, 6, 8]
total = 0

for num in list:
    total += num
print(f"The sum is: {total}")

list = [4, 5, 7, 8, 9, 1, 0, 7, 10]
list.sort()
prev = None
for item in list:
    if prev == item:
        print(f"Duplicate of {prev} found")
    prev = item

