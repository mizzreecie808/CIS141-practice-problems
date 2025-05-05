# Problem #7: Kitsap Rain Gear Advisor

is_raining = input("Is it raining? (yes/no) ")
temperature = float(input("What is the temperature? "))

if is_raining.lower() == "yes":
    if temperature >= 50:
        print("Umbrella")
    else:
        print("Rain jacket")
else:
    print("No rain gear needed.")



