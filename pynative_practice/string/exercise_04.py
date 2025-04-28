# https://pynative.com/python-string-exercise/
# Exercise 4: Arrange string characters such that lowercase letters come first
str = "PyNaTive"
answer = "yaivePNT"

def lower_first(s1):
    original = list(s1)
    lower = []
    upper = []
    for char in original:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)

    sorted = "".join(lower + upper)
    return sorted

result = lower_first(str)
print(result, result == answer)
