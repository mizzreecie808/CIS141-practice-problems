# Module 07 - Problem #5
'''
Write a function called level_up(experience) that takes a player's experience
points and returns their new level based on these rules:
* 0-99 XP → Level 1
* 100-199 XP → Level 2
* 200+ XP → Level 3
'''

def level_up(experience):
    if 0 <= experience <= 99:
        return "Level 1"
    elif 100 <= experience <= 199:
        return "Level 2"
    elif 200 <= experience:
        return "Level 3"
    else:
        return "Invalid input"

print(f" 98 XP -> {level_up(98)}")
print(f"198 XP -> {level_up(198)}")
print(f"298 XP -> {level_up(298)}")
print(f"-98 XP -> {level_up(-98)}")
