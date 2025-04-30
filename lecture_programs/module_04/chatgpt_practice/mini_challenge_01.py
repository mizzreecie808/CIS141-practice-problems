# ChatGPT 🌟 Practice Problems - Boolean
# Mini-Challenge #1

raining = input("Is it raining? (yes/no) ")
cold = input("Is it cold? (yes/no) ")
purpose = input("Is this a hiking or road trip? (hike/road) ")
age = int(input("How old are you? "))


if age < 18:
    if raining.lower() == "yes" and cold.lower() == "yes":
        print("You can't hike in this weather")
    elif raining.lower() == "no" and cold.lower() == "yes" and purpose.lower() == "road":
        print("Wear a jacket and take a road trip")
    else:
        print("You are too young to hike!")

else:
    if raining.lower() == "no" and cold.lower() == "no" and purpose.lower() == "hike":
        print("You can go hiking!")
    elif raining.lower() == "no" and cold.lower() == "yes" and purpose.lower() == "road":
        print("Wear a jacket and take a road trip.")
    else:
        print("Check your inputs")
