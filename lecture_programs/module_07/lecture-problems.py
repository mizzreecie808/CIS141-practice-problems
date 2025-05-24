# Module 07 Lecture Problems
# 01: Hello Kitsap!
def greet_city(city_name):
    print(f"Hello, {city_name.capitalize()}!")

# 02: OC Email Generator
def create_oc_email(first_name, last_name):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    return f"{first}{last}@student.olympic.edu"

# 03: Hike Elevation Gain
def elevation_gain(start_elev, end_elev):
    output = end_elev - start_elev
    print(f"Elevation gained: {output}")
    return output

# 04: Stardew Crop Profit
def crop_profit(sell_price, num_harvested):
    print(sell_price * num_harvested)
    return sell_price * num_harvested

# 05: Minecraft Tool Durability
def tool_durability(material, uses):
    output = f"Your {material.lower().strip()} tool has {uses} remaining."
    print(output)
    return(output)

# 06: Park Pass Discount
def calculate_fee(age, veteran):
    if age <= 12:
        cost = 0
    elif age > 12 and veteran:
        cost = 5
    else:
        cost = 10
    print(f"Park Fee: {cost}")
    return cost

# 07: Walking Speed Estimator
def estimate_walk_time(distance_miles, speed_mph):
    time_tw = round((distance_miles / speed_mph), 1)
    print(time_tw)
    return time_tw

# 08: OC Course Abbreviator
def abbreviate_courses(course_names):
    abbreviated = []
    for course in course_names:
        words = course.split()
        abbreviation = ""
        for word in words:
            abbreviation += word[0].upper()
        abbreviated.append(abbreviation)

    print(abbreviated)

college_courses = [
    "Software Engineering",
    "Version Control Collaboration",
    "Web Development",
    "DevOps Continuous Integration",
    "Integrated Development Environments"
]

# 09: Nature Vowel Counter
def count_vowels(plant_name):
    count = 0
    vowels = "aeiou"
    for letter in plant_name:
        if letter.lower() in vowels:
            count += 1
    return count

# 10: Inventory Value Checker
def total_inventory_value(inventory):
    return sum(inventory)

values = [57, 63, 72, 88, 95, 51, 68, 100]

# 11: Who Has the best GPA?
def compare_gpas(name1, gpa1, name2, gpa2):
    if gpa1 > gpa2:
        return name1
    elif gpa2 > gpa1:
        return name2
    else:
        return "Same GPA"

# 12: Top of the Trail - return a tuple name, est time hours, gain category
def trail_summary(trail_name, distance, gain):
    est_time = distance / 2 + (gain / 1000)
    gain_cat = ""

    if gain < 500:
        gain_cat = "low"
    elif 500 <= gain <= 1500:
        gain_cat = "moderate"
    else:
        gain_cat = "steep"

    return (trail_name, round(est_time, 2), gain_cat)

# 13: Daily Farm Report (Stardew)
# Return = "You harvest x crops" and "You fed Y animals"
def daily_farm_report(crops, animals):
    tasks = crops + animals
    msg1 = f"You harvested {crops} crops."
    msg2 = f"You fed {animals} animals."
    if tasks >= 10:
        busy = "Busy day!"
    elif 5 <= tasks <= 9:
        busy = "Nice and steady."
    else:
        busy = "Time for a break."

    return (msg1, msg2, busy)

# 14: Kitsap Weather Alert System
def check_alert(temp, wind, snow):
    if wind > 30:
        return "Wind advisory"
    elif temp < 32 and snow:
        return "Snow alert!"
    else:
        return "Conditions normal"

