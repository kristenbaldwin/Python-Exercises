# Exercise 1

name = input("What is your name? ")
print("Hello, {}!".format(name))

# Exercise 2

name = input("WHAT IS YOUR NAME? ")
name = name.upper()
name_length = len(name)
print(f"HELLO, {name}!")
print(f"YOUR NAME HAS {name_length} LETTERS IN IT! AWESOME!")

# Exercise 3

print("Please fill in the blanks below:____(name)____'s favorite subject in school is ____(subject)____.")
name = input("What is your name? ")
subject = input("What is your favorite subject? ")
print(f"{name}'s favorite subject in school is {subject}.")

# Exercise 4

day = int(input('Day (0-6)? '))
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(days_of_week[day])

# Exercise 5

day = int(input('Day (0-6)? '))
if day > 0 and day < 6:
    print("Go to work")
else:
    print("Sleep in")  

# Exercise 6

celsius = float(input('Temperature in C? '))
fahrenheit = celsius * 1.8 + 32
print(f"{fahrenheit} F")

# Exercise 7

total = int(input("Total bill amount? "))
level_of_service = input("Level of service? ")
if level_of_service == "good": 
    tip_amount = total * 0.20
elif level_of_service == "fair":
    tip_amount = total * 0.15
elif level_of_service == "bad":
    tip_amount = total * 0.10

bill_total = total + tip_amount
print("Tip amount: ${:.2f}".format(tip_amount))
print("Total amount: ${:.2f}".format(bill_total))

# Exercise 8

total = int(input("Total bill amount? "))
level_of_service = input("Level of service? ")
number_of_split = int(input("Split how many ways? "))
if level_of_service == "good": 
    tip_amount = total * 0.20
elif level_of_service == "fair":
    tip_amount = total * 0.15
elif level_of_service == "bad":
    tip_amount = total * 0.10

bill_total = total + tip_amount
per_person = bill_total / number_of_split
print("Tip amount: ${:.2f}".format(tip_amount))
print("Total amount: ${:.2f}".format(bill_total))
print("Amount per person: ${:.2f}".format(per_person))

# Exercise 9

count = 0
while count < 10:
    count += 1
    print(count)

# Exercise 10

coins = 0
another_coin = ''
print("You have 0 coins.")
while True:
    another_coin = input("Do you want another? ")
    if another_coin == "yes":
        coins += 1
        print(f"You have {coins} coins.")
    elif another_coin == "no":
        print("Bye")
        break