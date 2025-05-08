# ChatGPT 🔂 Nested For Loop Practice
# 5. Checkerboard Pattern
# # # #
 # # # #
# # # #
 # # # #
# # # #
 # # # #
# # # #
 # # # #

# my answer
# this is not alternating columns based on column index
# for row in range (4):
#     for column in range (4):
#         if row % 2 != 0:
#             print(" #", end = "")
#         else:
#             print("#", end = " ")
#     print()


# chat answer
# this alternates every cell both within rows and between rows
# this makes the characters alternate like a real checkerboard
for row in range (8):
    for column in range (8):
        if (row + column) % 2 == 0:
            print("#", end = "")    # Print # if the sum is even
        else:
            print(" ", end = "")    # Print space if the sum is odd
    print()
