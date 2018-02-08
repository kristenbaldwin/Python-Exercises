#Bonus Loop Exercise 3
#loop this: number % 2 == 0

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