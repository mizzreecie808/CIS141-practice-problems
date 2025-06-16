# ChatGPT - 🧩 Mini Challenge: Weather Analyzer
temperatures = [72, 68, 75, 70, 60, 65, 80]

# Print # of days where temp > 70
# Print highest and lowest temp for week
# Print Nice Week if all temp >=60 else Some chilly days

def temp_analyzer(temps):
    highest = max(temps)
    lowest = min(temps)
    nice_days = sum(1 for temp in temps if temp > 70)

    print("Weather Summary")
    print(f"Total days with temperature > 70: {nice_days}")
    print(f"Highest Temperature: {highest}")
    print(f"Lowest Temperature: {lowest}")
    
    if all(temp >= 60 for temp in temps):
        print("Nice Week!")
    else:
        print("Some chilly days")

temp_analyzer(temperatures)    