# Problem 3: Watchlist Gatekeeper
# Create a variable for the total episodes in a series.
# Set it to any number you want.
# Write a program that prompts the user for the number of
# episodes in the series they've watched.
# Display “Caught up” if both numbers match, otherwise “Keep watching!”.
episodes = 14
watched = int(input("How many episodes in the series have you already watched? "))

if episodes == watched:
	print("You're all caught up")
else:
	print(f"Keep watching, you have {episodes - watched} more episodes to go.")
