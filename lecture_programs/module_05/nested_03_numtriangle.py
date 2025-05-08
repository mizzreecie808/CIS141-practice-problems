# ChatGPT 🔂 Nested For Loop Practice
# 3. Triangle of numbers:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Step 1: use a loop to control the rows
# Step 2: for each row, print the numbers from 1 to row
# Step 3: move to the next line after each row
for row in range(1, 6):
    print(f"row: {row}")
    for num in range(1, row + 1):   # this increments
        print(num, end = " ")
    print()

