# Module 07 - Problem #2
# Write a function called is_palindrome(s) that checks whether a string is
# a palindrome (reads the same forward and backward, ignoring case).
# The function should return either True or False.

pal1 = "level"
pal2 = "rotator"
non_pal = "running"

def is_palindrome(input):
    # user lower() and strip() to make all lowercase and remove whitespaces
    forward = input.lower().strip()

    # input[::-1] reverses the string
    backward = input[::-1].lower().strip()

    # return gives either True or False based on the condition presented
    return forward == backward

print(f"Is {pal1} a palindrome?\t {is_palindrome(pal1)}")
print(f"Is {pal2} a palindrome?\t {is_palindrome(pal2)}")
print(f"Is {non_pal} a palindrome?\t {is_palindrome(non_pal)}")

