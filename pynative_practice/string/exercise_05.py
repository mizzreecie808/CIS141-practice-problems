# https://pynative.com/python-string-exercise/
# Exercise 5: Count all letters, digits, and special symbols
str = "P@#yn26at^&i5ve"

def count_all(s1):
    alpha = 0
    numeral = 0
    symbol = 0

    for char in s1:
        if char.isalpha():
            alpha += 1
        elif char.isdigit():
            numeral += 1
        else:
            symbol +=1

    result = f"""Total counts of chars, digits and symbols:
    Chars = {alpha}
    Digits = {numeral}
    Symbol = {symbol}
    """

    return result

print(count_all(str))
