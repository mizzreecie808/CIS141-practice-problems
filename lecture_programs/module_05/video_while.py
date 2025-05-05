# While Loops
# https://www.youtube.com/watch?v=eoEKSXkutfo

#while condition:
    # this code block
    # will be repeated
    # until condition is false

count = 0
while count < 5:
   print(f"The counter is at {count}")
   count += 1
print(f"The loop is finished at counter {count}.")

# Try to write a loop that counts down from 10 to 1

count = 10
while count >= 1: # or > 0
    print(count)
    count -= 1
print("The while loop is finished.")
