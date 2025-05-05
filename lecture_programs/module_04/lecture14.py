# Problem #14: Dungeon Door Puzzle

lever1 = input("Is lever 1 up? (yes/no) ").strip().lower() == "yes"
lever2 = input("Is lever 2 up? (yes/no) ").strip().lower() == "yes"
lever3 = input("Is lever 3 up? (yes/no) ").strip().lower() == "yes"

# door_opens = (
#     (lever1 and not lever2 and not lever3) or
#     (not lever1 and lever2 and not lever3) or
#     (not lever1 and not lever2 and lever3)
# )
# print("Door opens: ", door_opens)

door_opens = (lever1 + lever2 + lever3) == 1
print("Door opens: ", door_opens)
