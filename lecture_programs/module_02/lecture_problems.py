# Module 2 Lecture
# Problem #1 D&D Attribute CheckBox
# Create four variables for attributes of a new D&D character:
# her name is Saoirse; she's level 1; she has 12 hit points; she is a dwarf (race).
# Print out each variable’s value and its data type using type().
name, level, hit_points, race = "Saoirse", 1, 12, "Dwarf"
print("1)\t", type(name), type(level), type(hit_points), type(race))

# Problem #2 Anime Episodes
episodes, rating = 24, 8.7
print("2a)\t", type(episodes), type(rating))
episodes = str(episodes)
print("2b)\t", type(episodes), type(rating))

# Problem #3 Trail Distances
trail_miles = "8.5"
trail_km = float(trail_miles) * 1.60934
print("3)\t", type(trail_miles), trail_km, type(trail_km))

# Problem #4 Social-Media Username length
username = "gamerGirl42"
char_count = len(username)
print(f"4)\t {username} has {char_count} characters.")

# Problem #5 Muli-Dice Roll Setup
d6_1, d6_2, d6_3 = 0, 0, 0
print("5a)\t", d6_1, d6_2, d6_3)
d6_1, d6_2, d6_3 = 3, 4, 1
print("5b)\t", d6_1, d6_2, d6_3)

# Problem #6 Fix-That-Name
# Total$XP
# 1) Must start with letter or underscore
# 2) Cannot start with a number
# 3) Only alpha-numeric - no symbols allowed
total_xp = 1500
print("6\t", total_xp)

# Problem #7 Video-Game Hi-Score Swap
alice_score, bob_score = 9000, 7200
alice_score, bob_score = bob_score, alice_score
print(f"7)\t Alice has {alice_score} points and Bob has {bob_score} points")

# Problem #8 Outdoor Pace Calculator
distance_miles = 120 #float(input("How many miles did you travel?"))
time_minutes = 60 #int(input("How many minutes did it take you?"))
mph = distance_miles * (time_minutes / 60)
print(f"8)\t {mph:.1f} mph")

# Problem #9 Manga Page Timer
pages = 10 #int(input("How many pages?"))
minutes_per_page = 5 #float(input("How many minutes per page?"))
reading_time = (pages * minutes_per_page) / 60
print(f"9)\t You have read for {reading_time:.2f} hours.")

# Problem #10 Critical-Hit Percent
# print(f"Percentage: {0.75:.2%}")
hits, crits = 57, 12
crit_hit = crits / hits * 100
print(f"10)\t Critical rate: {crit_hit:.2f}%")

# Problem #11 Social-Media Character Limit
post = 290
twitter = post / 280 * 100
print(f"11)\t You used {twitter:.0f}% of Twitter's 280 characters.")

# Problem #12 Help-Hunt
# math.ceil rounds a number upward to the nearest integer
import math
# help(math.ceil)
print("12)\t math.ceil rounds a number upward to the nearest integer")

# Problem #13 Potion Splitter
potion, party = 23, 5
split, extra = (potion // party), (potion % party)
print(f"13)\t Each person will get {split} potions and {extra} potions will remain")

# Problem #14 Platformer Score Combo
print("14a)\t Original:\t", (10 + 5 * 2 ** 3 / 4))
print("14b)\t Parentheses:\t", ((10 + 5) * 2 ** 3 / 4))

# Problem #15 Mileage rounding
hiked = 5.7
print(f"15)\t You hiked {math.floor(hiked)} miles rounded down and {math.ceil(hiked)} miles rounded up.")

# Problem #16 Coffee-Shop Loyalty
name, drinks_purchased, price_per_drink = "Cerise", 6, 5.95
total = drinks_purchased * price_per_drink
print(f"16)\t {name} spent ${total:.2f} on {drinks_purchased} drinks.")

# Problem #17 Anime Binge Calculator
title, count, mpe = "Kikaida", 85, 33
total_hours = 85 * 33 / 60
print(f"17)\t It will take you {total_hours:.1f} hours to binge watch {title}.")

# Problem #18 Hike Elevation Gain
steps = 1342
step_conversion = 0.15 # meters
feet_conversion = 3.28084
total_meters = steps * step_conversion
total_feet = total_meters * feet_conversion
print(f"18)\t You hiked {total_meters:.2f} meters, which is equal to {total_feet:.2f} feet")

# Problem #19 D&D Dice Damage Simulator
num_dice, dice_sides = 3, 6
