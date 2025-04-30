# ChatGPT 🌟 Practice Problems - Boolean
# 5. **Number Guessing Feedback**

actual = 7
guess = int(input("Guess a number between 1 and 10: "))

if guess == actual:
    print("Correct!")
elif guess < actual:
    print("Too low!")
else:
    print("Too high!")
