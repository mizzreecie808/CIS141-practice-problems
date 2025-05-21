# ChatGPT - Functions
# 🧩 Function Exercise Set 2:
# Exercise 10 - Average Calculator
def calculate_average(nums):
    total = 0

    # handle an empty list
    if not nums:
        return 0

    for num in nums:
        total += num
    return total / len(nums)

sample_numbers = [10, 20, 30, 40, 50]  # Average should be 30.0
print(calculate_average(sample_numbers))

# Exercise 11 - Word Length Filter
def filter_long_words(words, length):
    longer = []

    for word in words:
        if len(word) > length:
            longer.append(word)

    return longer

sample_words = ["apple", "hi", "elephant", "sun", "rocket", "go"]
sample_length = 3  # Should return: ['apple', 'elephant', 'rocket']
print(filter_long_words(sample_words, sample_length))

# Exercise 12 - Simple Tip Calculator
def calculate_tip(total, percentage):
    tip = total * (percentage / 100)
    return round(tip, 2)

bill_total = 88.50
tip_percent = 18  # Should return: 15.93
print(calculate_tip(bill_total, tip_percent))

# Exercise 13 - Palindrome Checker
def is_palindrome(word):
    return word.lower().strip() == word[::-1].lower().strip()

test_words = ["Racecar", "banana", "level", "Python"]
# Racecar and level should return True, others False
for word in test_words:
    flag = is_palindrome(word)
    if flag == True:
        print(f"{word} is a Palindrome.")
    else:
        print(f"{word} is not a Palindrome.")

# Exercise 14 - Temperature Converter
def convert_temp(temp, scale):
    if scale == "C":
        conversion = (temp - 32) * (5 / 9)
        return f"{conversion:.1f}°C"
    elif scale == "F":
        conversion = (temp * (9 / 5)) + 32
        return f"{conversion:.1f}°F"
    else:
        return "Invalid scale, use 'C' or 'F'."

# Fahrenheit to Celsius
print(convert_temp(100, "C"))  # Should return 37.78 (approx)

# Celsius to Fahrenheit
print(convert_temp(0, "F"))  # Should return 32.0
