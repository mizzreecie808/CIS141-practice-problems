# ChatGPT 🎲 Challenge 8: Roll Until a 6
import random
# roll = 0
# counter = 0

# while roll != 6:
#     counter += 1
#     roll = random.randint(1, 6)
#     print(f"Roll #{counter}:{roll}")
# print(f"It took {counter} rolls to get to 6! Done!")

# last_roll = 0
# curr_roll = 0
# counter = 0

# while not (last_roll == 1 and curr_roll == 6): # not is important, else the loop will not run
#     last_roll = curr_roll               # shifts rolls foward
#     curr_roll = random.randint(1, 6)    # roll new to assign to curr_roll
#     counter += 1                        # increment counter
#     print(f"Roll #{counter}:{curr_roll}")
# print(f"It took {counter} rolls to get a 1 followed by a 6!")

# 🔀 Twist 1: Track All Rolls in a List
# 📊 Twist 2: Count How Many Times Each Number Was Rolled
# 🧠 Twist 3: Add a "Streak" Tracker
# 🎯 Twist 4: Add a User Guess Mode (Optional)
import random
user_guess = 4
last_roll = 0
curr_roll = 0
counter = 0
rolls = []
counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

current_streak = 1
longest_streak = 1

while not (last_roll == 1 and curr_roll == 6):
    last_roll = curr_roll
    curr_roll = random.randint(1, 6)
    rolls.append(curr_roll)
    counts[curr_roll] +=1
    counter += 1

    # Check for streaks
    if curr_roll == last_roll:
        current_streak += 1
    else:
        current_streak = 1

    # Update the longest streaks
    if current_streak > longest_streak:
        longest_streak = current_streak

    print(f"Roll #{counter}:{curr_roll}")

# Determine most rolled
most_rolled = max(counts, key = counts.get)

print(f"It took {counter} rolls to get a 1 followed by a 6!")
print(f"Roll sequence:\n{rolls}")
print(f"Number of times each number was rolled:\n{counts}")
print(f"Longest streak: {longest_streak}")
print(f"Most rolled: {most_rolled}")

# Check if the user guessed correctly
if user_guess == most_rolled:
    print(f"Congratulations, you guessed {most_rolled} correctly!")
else:
    print(f"Oops! You guessed wrong. The most rolled number was {most_rolled}.")
