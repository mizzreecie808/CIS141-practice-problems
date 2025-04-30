# ChatGPT 🌟 Practice Problems - Boolean
# 4. **Weather Clothing Suggestion**
raining = input("Is it raining (Yes/No)? ")
cold = input("Is it cold (Yes/No)? ")

if raining.lower() == "yes" and cold.lower() == "yes":
    print("Wear a raincoat and warm clothes!")
elif raining.lower() == "yes" and cold.lower() == "no":
    print("Take an umbrella!")
elif raining.lower() == "no" and cold.lower() == "yes":
    print("Wear a jacket!")
else:
    print("No special clothes needed!")
