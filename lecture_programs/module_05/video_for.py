# For Loops
# https://www.youtube.com/watch?v=3GGjW19JzXc
# iterate through sequence but don't know how many items in sequence

#for item in some_sequence:
    # do something

str = "Hello"
for char in str:
    print(f"{char}!")
print("Exited for loop")

# range(stop) -> range(5) -> 0, 1, 2, 3, 4
# range(start, stop) -> range(2, 6) -> 2, 3, 4, 5
# range(start, stop, step) -> range(2, 10, 2) -> 2, 4, 6, 8

for i in range(5):
    for j in range (5):
        print(f"({i}, {j})")
print("Exited for loop")

for i in range(0, 101, 2):
    print(i)
print("Exited for loop")

# Loop through the string "Programming" and print every 3rd letter
str = "Programming"
for i in range(0, len(str), 3):
    print(f"{i}: {str[i]}")
print("Exited for loop")
