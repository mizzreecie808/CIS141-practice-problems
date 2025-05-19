# ChatGPT ➕➖ Mini-Game #2: Math Word Puzzle
# List of number words and their corresponding numeric values
# The program randomly selects a word and shows it to the player
# The player inputs the numeric value they think matches the word
# The program checks if the guess is correct, and gives feedback
# Optionally, add hints or let the player try multiple times
import random

words = ["one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten"]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffled_words = ["eno", "otw", "eethr", "orfu", "vefi", "xsi", "evens",
                "gthei", "inne", "net"]

# Combine shuffled words and their corresponding values
combined = list(zip(shuffled_words, values))

wins = 0
losses = 0
games = 0
attempts = 0

while True:
    random.shuffle(combined)    # Shuffle at the start of each game
    # Counters for only current run of game
    current_wins = 0
    current_losses = 0

    print("\n🧠 Let's play! Decode the scrambled word into its correct number.\n")
    print("Type 'q' or 'quit' to exit anytime.\n")

    for word, correct_value in combined:
        guess = input(f"What number do you see? 🤔 {word} ➜ ").strip()

        # Exit condition
        if guess.lower() in ["q", "quit"]:
            print("👋 Game exited early.")
            break

        # Check if input is a digit
        if guess.isdigit():
            attempts += 1   # count the attempt
            if int(guess) == correct_value:
                print("✅ Correct!\n")
                current_wins += 1
            else:
                print(f"❌ Nope. The correct answer was {correct_value}.\n")
                current_losses += 1
        else:
            print("⚠️ Please enter a valid number.\n")

    # Update overall game total
    wins += current_wins
    losses += current_losses
    games += 1

    # Calculate average score safely
    # average_score = (wins / attempts) * 100 if attempts > 0 else 0
    if attempts > 0:
        average_score = (wins / attempts) * 100
    else:
        average_score = 0

    print(f"Game Over! You played {games} round(s).")
    print(f"✅ Correct answers:\t{wins}")
    print(f"❌ Incorrect answers:\t{losses}")
    print(f"🎯 Average score: {average_score:.0f}%\n")

   # Ask if user wants to play again
    play_again = input("🔁 Would you like to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print(f"Thanks for playing! You completed {games} round(s). 👋")
        break

















# Generate shuffled version of each word
# shuffled_words = []
# for word in words:
#     shuffled = "".join(random.sample(word, len(word)))
#     shuffled_words.append(shuffled)

# Combine into a single list of [scrambled_word, value] pairs
# combined = []

# for i in range(len(words)):
#     word = words[i]
#     value = values[i]

#     letters = list(word)
#     random.shuffle(letters)
#     scrambled = "".join(letters)

#     combined.append([scrambled, value])

# random.shuffle(combined)
