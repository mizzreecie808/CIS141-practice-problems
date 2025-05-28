print(len("Wednesday, (60.0°F)"))
print(len("--📋 Student Grades 📋--"))

def sum_num(num1, num2):
    return num1 + num2

sum_num(5, 10)
result = 15

def sum_product(num1, num2):
    total = num1 + num2
    product = num1 * num2
    return total, product

total, product = sum_product(3, 4)
print(total)
print(product)

def greet(name, greeting="Hello"):
    return f"{greeting.capitalize()} {name.capitalize()}!"

print(greet("cerise"))

def circle_math(rad):
    area = 3.14 * rad**2
    circ = 2 * 3.14 * rad
    return area, circ

print(circle_math(3))
