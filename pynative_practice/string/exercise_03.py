# https://pynative.com/python-string-exercise/
# Exercise 3: Create a new string made of the first, middle and last
# characters of each input string
str1 = "America"
str2 = "Japan"
answer = "AJrpan"

def new_string(s1, s2):

    mid1 = int(len(s1) / 2)
    mid2 = int(len(s2) / 2)

    str3 = str1[0] + str2[0] + str1[mid1] + str2[mid2] + str1[len(str1) - 1] + str2[len(str2) - 1]
    return str3

result = new_string(str1, str2)
print(result, answer == result)
