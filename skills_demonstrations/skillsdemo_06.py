# Module 06 Skills Demonstration
# Create a program that loops over a list and does something interesting
# with that list. Your program must be different than any of the
# Practice Problems or any code we covered together in the Lecture videos.
# Be creative! Try to personalize your program to your own life & interests.
# (Example: "A program that takes a list of Magic the Gathering card
# types in a deck of cards and calculates how many of each type is in the deck.")

adjectives = [
    "Fluffy", "Sneaky", "Speedy", "Sleepy", "Brave",
    "Tiny", "Loyal", "Fuzzy", "Gentle", "Spunky"]

animals = [
    "Panda", "Lizard", "Otter", "Fox", "Bunny",
    "Tiger", "Koala", "Penguin", "Ferret", "Turtle"]

print("My funny animals")

for i in range(len(adjectives)):
    funny_name = f"{adjectives[i]} the {animals[-(i + 1)]}"
    print(f"Presenting - {funny_name}")
