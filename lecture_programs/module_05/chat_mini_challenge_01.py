# ChatGPT 🕹️ Mini-Project - While Loops
# Mini-Challenge #1 - Number Guessing Game with hints
# generate random number
# ask user for guess
# after each guess tell them if too high or too low or correct
# keep track of how many guesses until they are correct
# add message if they guessed correct with the number of attempts
# track guesses
# warmer/colder hints

import random

# first while True statement asks user if they want to play again
while True:
    user_choice = input("Would you like easy/medium/hard?\t")
    if user_choice.lower() == "easy":
        computer = random.randint(1, 51)
        max_guesses = 10
        high = 50
    elif user_choice.lower() == "medium":
        computer = random.randint(1, 101)
        max_guesses = 7
        high = 100
    elif user_choice.lower() == "hard":
        computer = random.randint(1, 201)
        max_guesses = 5
        high = 200
    else:
        print("Invalid difficulty. Please choose easy, medium or hard.")
        continue

    count = 0
    prev_guess = None
    print(f"I'm thinking of a number between 1 and {high}.")
    print(f"You have {max_guesses} attempts to guess it.")

    while True:
        try:
            user = int(input("Guess: "))
            count += 1

            # Check if the guess is correct
            if user == computer:
                print(f"Correct! It took you {count} attempts.")
                break

            # Check if max guesses reached
            if count == max_guesses:
                print(f"You've exceeded the allowed attempts. The number was {computer} Goodbye!")
                break

            # Give warmer/colder feedback after the first guess
            if prev_guess is not None:
                prev_diff = abs(prev_guess - computer)
                current_diff = abs(user - computer)

                if current_diff < prev_diff:
                    print("Warmer")
                elif current_diff > prev_diff:
                    print("Colder")
                else:
                    print("Same distance as before.")

            # Keeps this for all guesses
            if user > computer:
                print("Too high")
            elif user < computer:
                print("Too low")

            # Save the current guess for the next round
            prev_guess = user

        except ValueError:
            print("Please enter a valid number.")

    # Ask user if they want to play again
    play_again = input("\nWould you like to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing! Goodbye 👋")
        break
