# ChatGPT 🌟 Practice Problems - Boolean
# Scenario-Challenges

# 1) Student must be under 25 or valid ID to get discount
age = 27
has_student_id = False

if age < 25 or has_student_id == True:
    print("You can get a discount")
else:
    print("Sorry, you can't get a discount.")

# 2) You can only hike if its not raining and you have at least one friend

is_raining = False
friends_coming = 0

if is_raining == False and friends_coming >= 1:
    print("You can go hiking")
else:
    print("Sorry, no hiking today.")

# 3) Special level if: 10+ coins and gold key or premium user

coins = 8
has_gold_key = True
is_premium_user = False

if (coins >= 10 and has_gold_key == True) or is_premium_user == True:
    print("You have unlocked the special level")
else:
    print("Sorry, no special level")

# 4) 18+ or VIP Ticket, but they must have ID if <21 or if <18 with adult
age = 20
has_vip = False
has_id = False
with_adult = True

if age > 18 or has_vip == True:
    if age < 21 and has_id == True:
        print("ENTER:\tunder 21 and has id")
    else:
        print("NO ENTRY:\tunder 21 and no id")
elif age < 18 and with_adult == True:
    print("ENTER:\tunder 18 and with adult")
else:
    print("NO ENTRY:\tunder 18, no vip, no adult")

# 5) Escape Room: all over 12, at least one over 18
person1_age = 14
person2_age = 17
person3_age = 19

all_over_12 = person1_age > 12 and person2_age > 12 and person3_age > 12
one_over_18 = person1_age > 18 or person2_age > 18 or person3_age > 18

if all_over_12 == True and one_over_18 == True:
    print("You can go into the escape room")
else:
    print("Sorry no escape room")
