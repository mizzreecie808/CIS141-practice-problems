# Reading - Debugging
# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Debugging

for i in range(10):
    if i == 5:
        continue
    print(f"i = {i}")
print("Outside the loop")
