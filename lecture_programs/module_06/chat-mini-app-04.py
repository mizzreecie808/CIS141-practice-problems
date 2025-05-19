# ChatGPT 🌡️ Mini App 4: Temperature Analyzer
# Ask the user to enter temperature readings
# (can be floats, like 72.5) for as many days as they want. Type 'done' to stop.
# Validation: Only accept valid numbers (positive or negative is okay).
# Storage: Save all the temperatures in a list.
# 🌡️ Number of temperature entries
# 📈 Highest and lowest temperature
# 🧮 Average temperature
# 🔥 How many days were above the average
# 🥶 How many days were below freezing (< 32°F)
# 📊 A sorted list of the temperatures (ascending)

# Simulated input list for testing
test_inputs = [
    "Monday, 70",
    "Tuesday, 72",
    "Wednesday, 75",
    "Thursday, 30",
    "Friday, 80",
    "Saturday, 65",
    "Sunday, 68",
    "done"
]

def get_input(prompt):
    """Simulates user input using a list. Falls back to real input
    if test_inputs is empty."""
    if test_inputs:
        value = test_inputs.pop(0)
        print(f"{prompt}{value}")  # Show what would have been typed
        return value
    else:
        return input(prompt)


temps = []
days = []

while True:
#     user_input = input("Enter a temperature (or type 'done'): ").strip().lower()
    user_input = get_input("Enter day and temperature (e.g., Monday, 72.5) or (type 'done'): ").strip().lower()

    if user_input == "done":
        entries = len(temps)
        highest = max(temps)
        hottest_day = days[temps.index(highest)]
        lowest = min(temps)
        coldest_day = days[temps.index(lowest)]
        average = sum(temps) / entries
        below_freezing = 0
        comfortable = 0
        above_avg = []

        for temp in temps:
            if temp > average:
                above_avg.append(temp)
            if temp < 32:
                below_freezing +=1
            if 65 <= temp <= 75:
                comfortable += 1

        # ^43 center align text
        print(f"\n{'🌡️ Temperature Summary 🌡':^43}️")
        print("━" * 43)
        print(f" {'Total Entries:':<20} {entries:>20}")
        print(f" {'Hottest Day:':<20} {f'{hottest_day}, ({highest:.1f}°F)':>20}")
        print(f" {'Highest Temperature:':<20} {highest:>18}°F")
        print(f" {'Lowest Temperature:':<20} {lowest:>18}°F")
        print(f" {'Average Temperature:':<20} {average:>18.1f}°F")
        print(f" {'Days above average:':<20} {len(above_avg):>20}")
        print(f" {'Days below freezing:':<20} {below_freezing:>20}")
        print("━" * 43)
        print(f"{'Daily Analysis':^43}")
        print("━" * 43)
        for i, (day, temp) in enumerate(zip(days, temps)):
            if temp == highest:
                symbol = "🌞"
            elif 65 <= temp <= 75:
                symbol = "✅"
            elif temp < 32:
                symbol = "🥶"
            else:
                symbol = ""
            daily_str = f"{day:<12} {temp:>8.1f}°F {symbol}"
            print(f"{daily_str:^43}")
        print("━" * 43)
        break

    parts = user_input.split(",")
    if len(parts) != 2:
        print("❌ Please enter input in the format: Day, Temperature (e.g., Monday, 72.5)")
        continue
    try:
        day_value = parts[0].strip().capitalize()
        temp_value = float(parts[1].strip())
        temps.append(temp_value)
        days.append(day_value)

    except ValueError:
        print("❌ Invalid input. Please enter a temerature (e.g., -15.2 or 75).")

