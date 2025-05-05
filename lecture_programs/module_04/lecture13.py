# Problem #13: Spoiler Filter

sentence = """She's not scared of taking risks.
I've had plenty of relationships that seemed like they'd work on paper,
but in practice, they were a bad idea. We've got much bigger problems to deal with.
The sponge absorbed the water quicker than the towel.
What would you no spoilers about yourself if you could change one thing?"""


if "spoiler" in sentence.lower() and "no spoilers" not in sentence.lower():
    print("Spoiler alert")
else:
    print("Safe to read")
