# Mod 7 Skills Demo Starter Code

def display_stats(name, vocation, level, health):
    display = f"{name} - Class: {vocation}, Level: {level}, Health: {health}"
    print(display)
    return display

# Generate stats for Warrior
warrior_name = "Thorin"
warrior_class = "Warrior"
warrior_level = 10
warrior_health = 150
formatted_stats = f"{warrior_name} - Class: {warrior_class}, Level: {warrior_level}, Health: {warrior_health}"
print("Generate stats for Warrior")
print(formatted_stats)
display_stats(warrior_name, warrior_class, warrior_level, warrior_health)
print()

# Generate stats for Mage
mage_name = "Merlin"
mage_class = "Mage"
mage_level = 12
mage_health = 120
formatted_stats = f"{mage_name} - Class: {mage_class}, Level: {mage_level}, Health: {mage_health}"
print("Generate stats for Mage")
print(formatted_stats)
display_stats(mage_name, mage_class, mage_level, mage_health)
print()

# Generate stats for Rogue
rogue_name = "Ezio"
rogue_class = "Rogue"
rogue_level = 8
rogue_health = 100
formatted_stats = f"{rogue_name} - Class: {rogue_class}, Level: {rogue_level}, Health: {rogue_health}"
print("Generate stats for Rogue")
print(formatted_stats)
display_stats(rogue_name, rogue_class, rogue_level, rogue_health)

