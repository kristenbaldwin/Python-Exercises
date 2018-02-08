# Exercise 1

for number in range(1, 11):
    print(number)

# Exercise 2

print("Start from: 2")
print("End on: 8")
for number in range(2, 9):
    print(number)

# Exercise 3

for number in range(1, 11, 2):
    print(number)

# OR 

for number in range(0, 10):
    if number % 2 != 0:
        print(number)

# Exercise 4

square = 0
while square < 5:
    square += 1
    print("*****")

# Exercise 5

count = 0
square = int(input("How big is the square? "))
while count < square:
    count += 1
    print("*" * square)

# Exercise 6

width = int(input("Width? "))
height = int(input("Height? "))
empty_space = width - 2
print("*" * width)
for i in range(0, height - 2):
    print("*", " " * empty_space, "*", sep="")
for i in range(height - 2, height - 1):
    print("*" * width)

# Exercise 7

lines = 0
empty = 0
for i in range(0, 4):
    lines += 1
    empty += 1
    blank_space = 4 - lines
    increase_char = lines + (lines - 1)
    print(" " * blank_space, "*" * increase_char, sep="")

# Exercise 8

height = int(input("Height? "))
lines = 0
empty = 0
for i in range(0, height):
    lines += 1
    empty += 1
    blank_space = height - lines
    increase_char = lines + (lines - 1)
    print(" " * blank_space, "*" * increase_char, sep="")

# Exercise 9

number1 = 1
number2 = 0
while number1 < 11:
    for number in range(0, 10):
        number2 += 1
        result = number1 * number2
        print(f"{number1} X {number2} = {result}")
    number1 += 1
    number2 = 0

# Bonus 1

text = input("Text? ")
border = len(text) + 2
print("*", "*" * border, "*", sep="")
print("*", text, "*")
print("*", "*" * border, "*", sep="")

# Bonus 2

count = 1
while count <= 100:
    for number in range(0, 100):
        triangle_number = int((count * (count + 1)) / 2)
        count += 1
        print(triangle_number)

# Bonus 3

number = int(input("Pick a number: "))
divide_by = 0
factors = []
while divide_by < number:
    for i in range(0, number):
        divide_by += 1
        divisiable = number % divide_by
        if divisiable == 0:
            factors.append(divide_by)
    print(factors)