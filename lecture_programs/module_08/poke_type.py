# Module 08 Lecture Problems
# 09: Pokemon Type Counter
file_name = "pokemon.txt"
poke_types = {}

with open(file_name, "r") as file:

    for line in file:
        pokemon = line.strip()
        if pokemon in poke_types:
            poke_types[pokemon] += 1
        else:
            poke_types[pokemon] = 1

    for pokemon, count in poke_types.items():
        print(f"{pokemon + ':':<10}{count:>4}")

