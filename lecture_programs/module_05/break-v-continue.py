# Break vs. Continue

# Break: exits the loop (breaks you out!)
#for i in range(10): #0 ... 9
#    if i == 5:
#        break
#    print("i=",i)
#print("Outside the for loop")

# Continue: skips the current iteration of  loop (continues to next iteration)
for i in range(10): #0 ... 9
    if i == 5:
        continue
    print("i=",i)
print("Outside the for loop")
