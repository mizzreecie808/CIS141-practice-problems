# ChatGPT 🎯 Mini-Game #1: Guess the Secret Word
# The computer picks a secret word (from a list).
# You get 5 tries to guess the word.
# After each wrong guess, you’re told how many tries are left.
# If you guess it right — you win!
import random
word_list = ["apple", "banana", "grape", "orange", "peach"]

while True:
    index = random.randint(0, len(word_list) - 1)
    secret_word = word_list[index]

    # add a scrambled word clue
    scrambled = list(secret_word)
    random.shuffle(scrambled)
    scrambled_clue = " ".join(scrambled)

    print("🍇 Welcome to Guess the Secret Word!")
    print("Guess the fruit! You have 5 tries.")
    print(f"🌀 Scrambled word clue: {scrambled_clue}")

    # reset the counter
    counter = 0

    while counter < 5:
        guess = input("Enter your guess: ").lower()
        counter += 1
        attempts = 5 - counter

        if guess == secret_word:
            print(f"🎯 Correct! You guessed the word {secret_word}! Thank you for playing!")
            break
        elif attempts > 0:
            print(f"❌ Wrong! {attempts} tries left.")
        else:
            print(f"💀 Game Over! The word was {secret_word}.")

    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != "yes":
        print("Thank you for playing. Good-bye!")
        break






# Guess the secret word! You have 5 tries.
# Enter your guess: banana
# Wrong! 4 tries left.
# Enter your guess: apple
# Wrong! 3 tries left.
# Enter your guess: peach
# Correct! You guessed the word!
