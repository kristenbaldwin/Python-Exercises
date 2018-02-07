my_list = [7, 2, -12, 15, 22, -3]

# Exercise 1

def list_sum(list):
    the_sum = 0
    for number in list:
       the_sum = the_sum + number
    return the_sum
print(list_sum(my_list))

# Exercise 2

my_list.sort()
print(my_list[-1])

# Exercise 3

my_list.sort()
print(my_list[0])

# Exercise 4

for number in my_list:
    if number % 2 == 0:
        print(number)

# Exercise 5

for number in my_list:
    if number > 0:
        print(number)

# Exercise 6

def pos_numbers(list):
    positives = []
    for number in list:
        if number > 0:
                positives.append(number)
    return positives
print(pos_numbers(my_list))

# Exercise 7

factor = 2
def multiply(list):
    new_list = []
    for number in list:
        new_number = number * factor
        new_list.append(new_number)
    return new_list
print(multiply(my_list))

# Exercise 8

list1 = [2, 3, 4]
list2 = [1, 5, 6]

list3 = []
for n in range(0, len(list1)):
    list3.append(list1[n] * list2[n])
print(list3)

# Exercise 9

matrix_list1 = [ [2, -2],
                [5, 3] ]
matrix_list2 = [ [1, 4],
                [-3, 2] ]
matrix_sum = [ [0, 0],
                [0, 0] ]

for r in range(len(matrix_list1)):
    for c in range(len(matrix_list1[0])):
        matrix_sum[r][c] = matrix_list1[r][c] + matrix_list2[r][c]

for x in matrix_sum:
    print(x)

# Exercise 10

matrix_list1 = [ [2, -2],
                [5, 3],
                [1, 6] ]
matrix_list2 = [ [1, 4],
                [-3, 2],
                [4, -1] ]
matrix_sum = [ [0, 0],
                [0, 0],
                [0, 0] ]

for r in range(len(matrix_list1)):
    for c in range(len(matrix_list1[0])):
        matrix_sum[r][c] = matrix_list1[r][c] + matrix_list2[r][c]

for x in matrix_sum:
    print(x)

# Exercise 11

dupe_list = ["dog", "cat", "bird", "dog", "pig", "turtle", "pig", "cat"]
def deduped(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
print(deduped(dupe_list))