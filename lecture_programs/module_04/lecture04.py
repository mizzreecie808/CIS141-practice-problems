# Problem 4: Hood Canal Tide Alert
# Ask for the current tide in feet (float)
# "Low tide - good time for beach-hiking." if below 4 ft
# "High tide - stay on the trail." otherwise

tide_height = float(input("What is the current tide height in feet? "))

if tide_height < 4:
	print("Low tide - good time for beach-hiking.")
else:
	print("High tide - stay on the trail.")
