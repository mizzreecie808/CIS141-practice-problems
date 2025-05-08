# Break vs. Continue
# https://www.youtube.com/watch?v=YhgHdWrm930

# Break: exits the loop (breaks you out!)
for i in range(10): # 0.....9
    if i == 5:
        print(f"i = {i} - Break!")
        break       # sends us out of this for loop
    print(f"i = {i}")
print("Outside the for loop")

# Continue: skips the current iteration of the loop (continues to next iteration)
for i in range(10): # 0.....9
    if i == 5:
        continue      # skips 5
    print(f"i = {i}")
print("Outside the for loop")
