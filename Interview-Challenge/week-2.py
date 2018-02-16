 # Challenge 1

num = int(input("Pick a number: "))
list1 = []
while num != 1:
    if num % 2 == 0:
        num = int(num / 2)
        list1.append(num)
    elif num % 2 != 0:
        num = int((num * 3) + 1)
        list1.append(num)
print(list1)

# Challenge 2

counter1 = 999
counter2 = 999
pal_list = []

while counter1 > 100:
    while counter2 > 100:
        list1 = []
        list2 = []
        pal = counter1 * counter2
        pal = str(pal)
        if len(pal) == 6:
            for i in range(0,3):
                list1.append(pal[i])
            for i in range(3,6):
                list2.append(pal[i])
            list2.reverse()
            #print(list1 + list2)
        else:
            break
        if list1 == list2:
            list2.reverse()
            pal = ''.join(list1 + list2)
            #print(pal)
            pal_list.append(pal)
            #print(pal_list)
            break
        else:
            counter2 -= 1
    counter1 -= 1
    counter2 = counter1
pal_list.sort()
print(pal_list[-1])

 
'''Alternative Method
counter1 = 999
counter2 = 999
pal_list = []
def reversed(x):
    return x[::-1]

while counter1 > 100:
    while counter2 > 100:
        list1 = []
        list2 = []
        pal = counter1 * counter2
        pal = str(pal)
        list1.append(pal[0:3])
        list2.append(pal[3:6])
        str1 = "".join(list2)
        list2 = reversed(str1)
        last3_nums = list2
        first3_nums = "".join(list1)
    
        if first3_nums == last3_nums:
            last3_nums = reversed(last3_nums)
            pal = first3_nums + last3_nums
            pal_list.append(pal)
            #print(pal_list)
            break
        else:
            counter2 -= 1
    counter1 -= 1
    counter2 = counter1
pal_list.sort()
print(pal_list[-1])  
'''  

# Challenge 3

x = 2520
divisiable_by = 11

while divisiable_by <= 20:
    if x % divisiable_by == 0:
        divisiable_by += 1
    else:
        x += 1
        divisiable_by = 11

print(x)
