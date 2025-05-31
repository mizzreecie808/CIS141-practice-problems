# Video - Problem solving text files
# Write a Python program that allows a baker to log orders from customers.
# The program should:
# - Open orders.txt (append mode)
# - Use a while loop to repeatedly ask for customer names & orders
# - Save each entry to orders.txt (each order on a new line)
# - When the user presses 0, exit the loop & print the contents of orders.txt
# - Close orders.txt when I'm done

file = open("orders.txt", "w")
file.write("")
file.close()

# creates access to file
file = open("orders.txt", "a")

while True:
    name = input("What is the customer's name? Press 0 to exit. ")

    if name == "0":
        print("Thank you, exiting program.")
        break

    order = input("What is the customer's order? Press 0 to exit. ")

    if order == "0":
        print("Thank you, exiting program.")
        break

    file.write(f"{name}\t{order}\n")

file.close()
