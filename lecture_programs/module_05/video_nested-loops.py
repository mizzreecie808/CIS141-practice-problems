# Nested Loops
# https://www.youtube.com/watch?v=rUjN2WxvNbc

# for i in range(3):      # Outer loop (0, 1, 2)
#     for j in range(2):  # Inner loop (0, 1)
#         print(f"({i},{j})")
#     print("Exiting inner loop")
# print("Exiting outer loop")

#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

for i in range(5):          # Outer loop (0, 1, 2, 3, 4)
    for j in range(5):      # Inner loop (0, 1, 2, 3, 4)
        print(j + 1, end=" ")
    print("")
