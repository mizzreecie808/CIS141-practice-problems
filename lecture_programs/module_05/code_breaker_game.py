# ChatGPT 🧩 Challenge: Code Breaker Game
# Player must guess a 4-digit secret code
# Each digit between 1 and 6
# Unlimited attempts, but program must track the number of attempts
# After each guess provide feedback on each digit:
# "Correct" if digit correct and right position
# "Wrong" if digit is incorrect or in wrong position
# Example [2, 5, 3, 1] User 2532
# 1: Correct 2: Correct 3: Correct 4: Wrong
# Ask user for guess, but must be exactly 4 digits
# While loop to keep going until 100% correct
# Use for loop to check each digit and print "Correct" or "Wrong"
# Count how many attempts the user took
# Use booleans or conditions to track when the guess is fully correct

import random

# --- Difficulty Selection ---
print("🧩 Challenge: Code Breaker Game")
print("Choose a level: Easy (E), Medium (M), Hard (H): ")
difficulty = input("Your choice: ").lower()

if difficulty == "e":
    code_length = 3
    max_attempts = None
elif difficulty == "m":
    code_length = 4
    max_attempts = None
elif difficulty == "h":
    code_length = 6
    max_attempts = 10
else:
    print("Invalid choice. Defaulting to Medium.")
    code_length = 4
    max_attempts = None

# --- Generate Secret Code ---
secret_code = [random.randint(1, 6) for _ in range(code_length)]
print(secret_code)

# --- Game Loop ---
counter = 0
guess = []

while guess != secret_code:
    counter += 1

    # Check if attemp limit if on hard mode
    if max_attempts and count > max_attempts:
        print("❌ Too many attempts! Game over.")
        print(f" The code was: {secret_code}")
        break

    # Get user guess
    user_input = input(f"Enter a {code_length}-digit guess (digits 1-6): ")

    # Validate input is 4 digits and only numbers
    while len(user_input) != code_length or not user_input.isdigit():
        user_input = input(f"Invalid. Enter exactly {code_length} digits: ")

    # Convert user_input to list of integers
    guess = [int(d) for d in user_input]

    for i in range(code_length):
        if guess[i] == secret_code[i]:
            print(f"Digit {i + 1}: Correct")
        else:
            print(f"Digit {i + 1}: Wrong")

else:
    print(f"🎉 You cracked the code {secret_code} in {counter} tries!")
