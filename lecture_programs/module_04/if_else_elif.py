# If, Else, Elif and Indentation
# https://www.youtube.com/watch?v=JgVSmJFmvvw
# Common pitfalls
# Don't capitalize if, elif, else
# Indentation matters, if you don't indent, you will likely get an error
# Don't forget the colon after condition

# Comparison Operators Refresher: < > <= >= != ==
print("Comparison Operators")
print(4 > 3)
print(4 == 3)
print("-" * 40)

# Basic if Statement
print("Basic if Statement")
temperature = 85
if temperature > 75:
    print(f"It's {temperature} degrees and beautiful outside!")
print("-" * 40)

# Basic if else Statement
print("Basic if else Statement")
temperature = 65
if temperature > 75:
    print(f"It's {temperature} degrees and beautiful outside!")
else:
    print(f"It's {temperature} degrees and too chilly out!")
print("-" * 40)

# if-elif-else Statement
print("if-elif-else")
temperature = 51
if temperature > 80:
    print(f"It's {temperature} degrees and beautiful outside!")
elif temperature > 60:
    print(f"It's {temperature} degrees and you should wear a jacket!")
else:
    print(f"It's {temperature} degrees and too chilly out!")
print("-" * 40)
