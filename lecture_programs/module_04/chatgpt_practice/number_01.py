# ChatGPT 🌟 Practice Problems - Boolean
# 1. **Check if a Number is Positive and Even**
num = int(input("Enter a number, any number: "))

if (num > 0) and (num % 2) == 0:
    print(f"{num} is both positive and even.")
elif num > 0 and (num % 2) != 0:
    print(f"{num} is postive, but not even.")
else:
    print(f"{num} is negative")
