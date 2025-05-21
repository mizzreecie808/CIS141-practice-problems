# Module 07 - Problem #4
'''
Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare based on age and whether the person has a vehicle.
Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
'''

def ferry_fare(age, vehicle):
    if age <= 18:
        return 0

    if vehicle:
        if 19 <= age <= 64:
            return 20
        else:
            return 15
    else:
        if 19 <= age <= 64:
            return 10
        else:
            return 5

# Test all logic statements
print(f"Age 38 with vehicle:\t${ferry_fare(38, True)}")
print(f"Age 38 no vehicle:\t${ferry_fare(38, False)}")

print(f"Age 71 with vehicle:\t${ferry_fare(71, True)}")
print(f"Age 71 no vehicle:\t${ferry_fare(71, False)}")

# Will be $0 whether vehicle is true or false
print(f"Age 17 with vehicle:\t${ferry_fare(17, True)}")
print(f"Age 17 no vehicle:\t${ferry_fare(17, False)}")
