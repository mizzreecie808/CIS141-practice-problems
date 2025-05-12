# ChatGPT 🌟 Challenge 2: FizzBuzz Lite (for loop)
# Loop through 1 to 30
# If divisible by 3, print "Fizz"
# If divisible by 5, print "Buzz"
# If divisible by 3 & 5, print "FizzBuzz"
# Otherwise print number

for num in range(1, 31):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
