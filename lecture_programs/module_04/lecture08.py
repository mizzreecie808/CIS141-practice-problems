# Problem #8: DND Encumbrance Calculator

strength = int(input("What is your strength score? "))
weight = float(input("What is your carried weight? "))
threshold = strength * 15

if weight > threshold:
    print("Encumbered")
else:
    print("Free to move")
