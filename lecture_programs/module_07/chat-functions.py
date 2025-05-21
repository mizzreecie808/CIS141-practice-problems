# ChatGPT - Functions
# ✅ Stage 1: Function Basics
# Exercise 1 - Greet User
def greet_user(name):
    print(f"Hello, {name}! Welcome back.")

# greet_user("Alice")

# Exercise 2 - Add numbers
def add_numbers(x, y):
    return x + y

# output = add_numbers(5, 7)
# print(output)

# Exercise 3 - Is even
def is_even(num):
    return num % 2 == 0

# print(is_even(1))
# print(is_even(2))

# ✅ Stage 2: Functions with Logic & Loops
# Exercise 4 - Repeated message
def repeat_message(msg, num):
    repeat_str = msg * num
    print(repeat_str)

# repeat_message("Hello!", 5)

# Exercise 5 - Count vowels

def count_vowels(word):
    count = 0
    # Strings behave like a list of characters, can loop over them directly
    for char in word:
        if char.lower() in "aeiou":
            count += 1
    return count

# vowel_count = count_vowels("Hello")
# print(vowel_count)

# Exercise 6 - Take a list and return max value

nums = [1, 5, 70, -10, 2]

def get_max(lst):
    highest = lst[0]
    for num in lst:
        if num >= highest:
            highest = num
    return highest

# max_num = get_max(nums)
# print(max_num)

# ✅ Stage 3: Function-Based Mini Tools
# Exercise 7 - List of numbers and returns a tuple
nums = [1, 5, 70, -10, 2]

def get_summary_stats(lst):
    total = 0
    highest = lst[0]
    lowest = lst[0]

    for num in lst:
        total += num
        if num >= highest:
            highest = num
        if num <= lowest:
            lowest = num

    average = total / len(lst)

    return total, average, highest, lowest

# summary = get_summary_stats(nums)
# print(summary)

# Exercise 8 - Print box of *
# def print_box(width, height):
#     for i in range(width):


# Exercise 9 - Strong password
def check_password_strength(password):

    over_eight = len(password) >= 8
    has_number = False
    has_upper = False

    for char in password:
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_upper = True
    if over_eight and has_number and has_upper:
        return "Strong"
    else:
        return "Weak"

# while True:
#     password = input("Enter a password: ")
#     strength = check_password_strength(password)

#     if strength == "Strong":
#         print("Password is strong. ✅")
#         break
#     else:
#         print("Password is weak. ❌ Please try again.")

# Exercise 9a - Strong password with feedback
def check_password(password):

    feedback = []

    # Check for length
    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long.")

    # Check for numbers
    has_number = any(char.isdigit() for char in password)
    if not has_number:
        feedback.append("Password must include at least one number.")

    # Check for uppercase
    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        feedback.append("Password must include at least one uppercase letter.")

    if not feedback:
        return "Strong"
    else:
        return "Weak", feedback

while True:
    password = input("Enter a password: ")
    result = check_password(password)

    if result == "Strong":
        print("Password is strong. ✅")
        break
    else:
        print("Password is weak. ❌")
        # result is a tuple: ("Weak", [list of reasons])
        for message in result[1]:
            print("-", message)
        print()


