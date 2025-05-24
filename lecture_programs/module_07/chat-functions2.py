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
# print(calculate_average(sample_numbers))

# Exercise 11 - Word Length Filter
def filter_long_words(words, length):
    longer = []

    for word in words:
        if len(word) > length:
            longer.append(word)

    return longer

# sample_words = ["apple", "hi", "elephant", "sun", "rocket", "go"]
# sample_length = 3  # Should return: ['apple', 'elephant', 'rocket']
# print(filter_long_words(sample_words, sample_length))

# Exercise 12 - Simple Tip Calculator
def calculate_tip(total, percentage):
    tip = total * (percentage / 100)
    return round(tip, 2)

# bill_total = 88.50
# tip_percent = 18  # Should return: 15.93
# print(calculate_tip(bill_total, tip_percent))

# Exercise 13 - Palindrome Checker
def is_palindrome(word):
    return word.lower().strip() == word[::-1].lower().strip()

test_words = ["Racecar", "banana", "level", "Python"]
# Racecar and level should return True, others False
# for word in test_words:
#     flag = is_palindrome(word)
#     if flag == True:
#         print(f"{word} is a Palindrome.")
#     else:
#         print(f"{word} is not a Palindrome.")

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
# print(convert_temp(100, "C"))  # Should return 37.78 (approx)

# Celsius to Fahrenheit
# print(convert_temp(0, "F"))  # Should return 32.0

# Exercise 15 - Word Counter
def count_words(sentence):
    words = sentence.split()
    total = len(words)
    print(f"Word Count: {total}")
    return total

# sentence = "The del keyword removes the   item with the   specified key name:"
# count_words(sentence)

# Exercise 16 - Score Categorizer
def categorize_score(score):
    cats = ["Invalid Input","Fail", "Pass", "Excellent"]

    if not 0 <= score <= 100:
        return cats[0]
    elif score >= 80:
        return cats[3]
    elif score >= 60:
        return cats[2]
    else:
        return cats[1]

# print(categorize_score(81))
# print(categorize_score(71))
# print(categorize_score(51))
# print(categorize_score(-81))

# Exercise 17 - Find Common Elements
def find_common(list1, list2):

    # Empty list to store commons
    common = []

    for item in list1:
        if item in list2:
            common.append(item)

    # Removes duplicates before returning
    return list(set(common))

# print(find_common([1, 2, 2, 3, 4], [2, 4, 4, 6]))  # Expected: [2, 4]

# Exercise 18 - Evens
def get_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens

def get_evens_compact(nums):
    return list({num for num in nums if num % 2 == 0})

# sample_nums = [3, 8, 12, 5, 7, 10, 21]
# print(get_evens(sample_nums))
# print(get_evens_compact(sample_nums))

# Exercise 19 - Remove duplicates
def remove_duplicates(lst):
    # sorted() alphabetizes list
    # list() converts the set back to a list
    # set() converts list to set which automatically removes duplicates
    return sorted(list(set(lst)))

def remove_duplicates_preserve_order(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

# sample_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
# print(remove_duplicates(sample_list))
# print(remove_duplicates_preserve_order(sample_list))

# Exercise 20 - Reverse List
def reverse_list(lst):
#     return list(reversed(lst))
    return lst[::-1]

nums = [1, 2, 3, 4, 5]
print(reverse_list(nums))
