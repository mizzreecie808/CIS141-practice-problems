# Module 08 Lecture Problems
# 06: Minecrat Block Logger
# Torch at (10, 66)
# Cobblestone at (13, 64)
file_name = "blocks.txt"

with open(file_name, "a") as file:
    block_type = input("What block did you place?\t")
    location = input("Where? 'X:50 Y:100':\t")
    coords = location.split(" ")
    print(coords)

    block_placed = f"{block_type.capitalize()} at ({coords[0]}, {coords[1]})"
    file.write(block_placed + "\n")

with open(file_name, "r") as file:
    print(f"{'Minecraft Block Log':^30}")
    print("🟩⛏️🟫" * 3)
    for line in file:
        print(line.strip())
