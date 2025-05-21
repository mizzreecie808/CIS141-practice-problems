# Module 07 - Problem #3
'''
In the game Pokemon, certain types of Pokemon do extra damage to other types.
For example, water is very effective to fight fire.
Write a function called type_advantage(attacker, defender) that takes two
Pokémon types as strings and returns "Super Effective", "Not Very Effective",
or "Neutral" based on simple type effectiveness rules. Your solution only
needs to work for these three sets of input:
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"
'''

type_elec = "Electric"
type_fire = "Fire"
type_grass = "Grass"
type_water = "Water"

def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"
    elif attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    elif attacker == "Electric" and defender == "Grass":
        return "Neutral"
    else:
        return "Invalid entries"

print(f"{type_water} attacks {type_fire} is {type_advantage(type_water, type_fire)}")
print(f"{type_fire} attacks {type_water} is {type_advantage(type_fire, type_water)}")
print(f"{type_elec} attacks {type_grass} is {type_advantage(type_elec, type_grass)}")

