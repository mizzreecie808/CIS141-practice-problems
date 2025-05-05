# Problem #6: Game XP Level Up
# User input their current XP (int)

xp = int(input("What is your current XP? "))

if xp >= 1000:
	print("Level Up!")
elif 700 <= xp < 1000:
	print("Almost there.")
else:
	print("Keep grinding.")
