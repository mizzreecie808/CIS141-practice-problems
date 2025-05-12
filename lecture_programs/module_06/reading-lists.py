# Reading - Lists
# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Lists

# which_one = int(input("What month (1-12)? "))
# months = ["January", "February", "March", "April", "May", "June", "July", 
#           "August", "September", "October", "November", "December"]
# if 1 <= which_one <= 12:
#     print(f"The month is: {months[which_one - 1]}")

demolist = ["life", 42, "the universe", 6, "and", 9]
# print(f"demolist = {demolist}")

# demolist.append("everything")
# print(f"after 'everything' was appended, demolist is now: {demolist}")

# print(f"len(demolist) = {len(demolist)}")
# print(f"demolist.index(42) = {demolist.index(42)}")
# print(f"demolist[1] = {demolist[1]}")

# for c in range(len(demolist)):
#     print(f"demolist[{c}] = {demolist[c]}")

# better way then above
for index, x in enumerate(demolist):
    print(f"demolist[{index}] = {x}")

# del demolist[2]
# print(f"After 'the universe' was removed demolist is now: {demolist}")

# if "life" in demolist:
#     print("'life' was found in demolist")
# else:
#     print("'life' was not found in demolist")

another_list = [42, 7, 0, 123]
another_list.sort()
print(f"The sorted another_list is: {another_list}")