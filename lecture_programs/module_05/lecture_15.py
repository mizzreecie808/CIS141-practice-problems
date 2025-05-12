# Module 05 Lecture Problem #15
# Create a table that helps someone visulaize how much they would earn
# in a year (before taxes) for different numbers of hours worked each week
# and different hourly wages
# Use these hours per week: 15, 20, 25, 30
# Use these wages: 19, 21, 23, 25
# assume 48 weeks per year

hours_per_week = [15, 20, 25, 30]
wages_per_hour = [19, 21, 23, 25]
weeks = 48

# Header row
print("\t\t", end = "")
for wages in wages_per_hour:
    print(f"${wages}/hr\t", end = "")
print()

for hours in hours_per_week:
    print(f"{hours}hrs/week\t", end = "")
    for wages in wages_per_hour:
        print(f"${hours * wages * weeks}", end = "\t")
    print()
