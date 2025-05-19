# Module 06 Lecture Problems
# 01: Hiking Gear
# gear = ["Backpack", "Water Bottle", "Map", "Compass"]
# print(f"Hiking Gear total: {len(gear)}")

# 02: Indexing Pokémon
# team = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"]
# print(f"First:\t {team[0]}")
# print(f"Last:\t {team[-1]}")

# 03: Minecraft Biomes
# biomes = []
# while len(biomes) < 3:
#     biome_input = input("Enter a name: ")
#     biomes.append(biome_input)
# print(biomes)

# 04: Stardew Valley Crops
# crops = ["Parsnip", "Potato", "Kale"]
# crops.append("Caulifower")
# print(crops)

# 05: Class Schedule
# classes = ["CIS141", "CIS155", "CS243"]
# print(classes)
# classes.insert(1, "CIS101")
# print(classes)

# 06: Trail List
# trails = ["Green Mountain", "Dickerson Creek", "Fort Ward", "Clear Creek"]
# print(trails)
# trails.remove("Fort Ward")
# print(trails)

# 07: Minecraft Inventory
# inventory = ["Wood", "Stone", "Iron", "Diamond"]
# print(inventory)
# popped_item = inventory.pop()
# print(popped_item)
# print(inventory)

# 08: Daily Chores
# chores = ["Feed cat", "Wash dishes", "Take out trash"]
# print(chores)
# del chores[1]
# print(chores)

# 09: Club Names
# clubs = ["Women in Tech", "Robotics", "Gamers"]
# print(clubs)
# clubs[0] = clubs[0].upper()
# print(clubs)

# 10: Subset of Trails
# trails = ["Fort Ward", "Dickerson Creek", "Green Mountain", "Newberry Hill Heritage Park"]
# subset = trails[1:3]
# print(trails)
# print(subset)

# 11: Temperature Alerts
# temps = [48, 55, 62, 45, 50]

# for temp in range(len(temps)):
#     if temps[temp] < 50:
#         print(f"{temps[temp]} Carry a Jacket!")
#     else:
#         print(temps[temp])

# 12: Hiking Distances
# distances = [3.2, 5.1, 4.8, 6.0]
# shortest = min(distances)
# longest = max(distances)
# average_dist = sum(distances) / len(distances)
# print(f"Shortest hike:\t{shortest}")
# print(f"Longest hike:\t{longest}")
# print(f"Average hike:\t{average_dist:.1f}")

# 13: Volunteer Hours
# hours = [2, 5, 1, 4, 3]
# print(hours)
# hours.sort()
# print(hours)

# 14: Course Codes
# codes = ["CS243", "CIS141", "CIS155", "CS110", "CS233", "CS111"]
# print(codes)
# sorted_codes = sorted(codes)
# print(sorted_codes)

# 15: Favorite Games
# games = ["Minecraft", "Pokemon", "Raft", "Animal Crossing", "Stardew Valley"]
# print(games)
# games.reverse()
# for i in range(len(games)):
#     games[i] = games[i].lower()
# print(games)

# 16: Finding a Trail
# trails = ["Fort Ward", "Dickerson Creek", "Green Mountain", "Newberry Hill Heritage Park"]
# trail_check = "Clear Creek"
# if trail_check in trails:
#     print(f"{trail_check} at index: {trails.index(trail_check)}")
# else:
#     print("Trail not in list")

# 17: 10,000 steps a day
# steps = [3200, 10500, 8700, 12300, 4500, 9800]
# print(steps)

# for i in range(len(steps)):
#     if steps[i] > 10000:
#         steps[i] = 10000
# print(steps)

# 18: Filter Out Low Pokemon Levels
levels = [5, 12, 3, 20, 8, 1, 15]
print(levels)
i = 0
while i < len(levels):
    if levels[i] < 5:
        levels.pop(i)
    else:
        i += 1
print(levels)
