# Problem #16: Infulencer Analytics

follower_count = 1000 #int(input("Follower count: "))
eng_rate = 14 #float(input("Engagement rate (%): "))

if follower_count >= 1000000 or eng_rate >= 15:
    category = "Mega"
    desc = "You command a large widespread audience."
elif follower_count >= 100000 and eng_rate >= 5:
    category = "Macro"
    desc = "You have a good balance of reach and engagement."
elif follower_count >= 10000 and eng_rate >= 2:
    category = "Micro"
    desc = "You have high engagement rates and authenticity."
else:
    category = "Nano"
    desc = "You have strong connections with niche audiences."

print(f"Category: {category} - {desc}")
