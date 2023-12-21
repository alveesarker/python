# i = 1
# b = []
# while i <= 10:
#     marks = int(input())
#     if 0 <= marks <= 100:
#         b.append(marks)
#     else:
#         continue
#     i += 1
# b.sort()
# print(b)
# print(len(b))
# x = max(b)
# y = min(b)
# print(x)
# print(y)
# count= 0
# for i in b:
#     if i < 50:
#         count += 1
# print(count)
# print(f"{(count / 10) * 100}%")
# j = 0
# while j < count:
#     b.remove(b[0])
#     j += 1
# print(b)
# for k in b:
#     print(k)

# def aflkj(a, *b, c= 0):
#     print(a, b, c)
# aflkj(1, 2, 3, c=4)

# def getCustomerName():
#     name = input('Name: ')
#     return name
# def getCustomerID():
#     id = int(input('C ID: '))
#     return id
# def getPurchageAmount():
#     total_amount = 0
#     total_items = int(input('Total Items: '))
#     for item in range(total_items):
#         item_amount = int(input("Item amount: "))
#         total_amount += item_amount
#     return total_amount
# def discount(purchaseAmount):
#     if(purchaseAmount > 15000):
#         final_amount = purchaseAmount *.7
#     elif (purchaseAmount > 10000):
#         final_amount = purchaseAmount *.8
#     else:
#         final_amount = purchaseAmount
#     return final_amount
# def printPurchaseInfo(*allInfo):
#     for info in allInfo:
#         print(info)
# name = getCustomerName()
# id = getCustomerID()
# buyAmount = getPurchageAmount()
# payableAmount = discount(buyAmount)
# printPurchaseInfo(name, id, buyAmount, payableAmount)


# rows = 4
# k = 0
# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print(end=" ")
#     while k!=(2*i-1):
#         print("* ", end="")
#         k += 1
#     k = 0
#     print()

# n = int(input())
# for i in range(n):
#     for k in range(n-i):
#         print(i+1, end=' ')
#     print()


# def grade(mark):
#     if mark>=80 and mark<=100:
#         g = "A"
#     elif mark>=60 and mark<=79:
#         g = "B"
#     elif mark>=40 and mark<=59:
#         g = "C"
#     elif 0 <= mark <= 39:
#         g = "F"
#     return g

#
# results_list = [[1234111, 'A', 73],
#                 [1234222, 'W', 17],
#                 [1234333, 'W', 57],
#                 [1234444, 'A', 89],
#                 [1234555, 'A', 32]]
# for i in range(len(results_list)):
#     if results_list[i][1]=="W":
#         print(results_list[i][0], results_list[i][1])
#     else:
#         print(results_list[i][0], grade(results_list[i][2]))

# for i in range(len(results_list)):
#     if results_list[i][1] != "W":
#         print(results_list[i][0], grade(results_list[i][2]))


# a = [7, 5, 1, 10, 9, 9, 6, 6, 8, 20]
# a.insert(4, 20)
# a.append(20-2)
# print(a)
# b = a.pop()
# print(b)
# c = a.count(20)
# print(c)

# def printnumber(x):
#     for i in range(x):
#         print(i, end =' ')
#     return
# lines = int(input('How many lines to print:'))
# while lines > 0:
#     printnumber(lines)
#     print()
#     lines -= 1


# def getItemQty():
#     qty = int(input('How Many item to purchase: '))
#     unitPrice = int(input('unit Price: '))
#     return [qty,unitPrice]
# def calculatePrice(varArgs):
#     total = varArgs[0] * varArgs[1]
#     return total
# def printAll(qty, uPrice, total):
#     print(f'QTY: {qty} \nUnit Price: {uPrice} \nPayable: {total}')
# detail = getItemQty()
# price = calculatePrice(detail)
# printAll(detail[0],detail[1],price)

# a = [5, 2, 3, 6, 4, 1]
# even = 0
# odd = 0
# i = 0
# while i < len(a):
#     row = a[i]
#     if row % 2 == 0:
#         print('even: ', row)
#         even += row
#     else:
#         print('odd: ', row)
#         odd += row
#     i += 1
# print(f'Even addition: {even} \nOdd addition: {odd}' )

# def averageMarks(mark_list):
#     a = sum(mark_list)/ len(mark_list)
#     return a


# def add(x, y):
#     b = x + y
#     return b
# def sub(x, y):
#     c = x - y
#     return c
# def mul(x, y):
#     d = x * y
#     return d
# def div(x, y):
#     e = x / y
#     return e
#
# while True:
#     choice = input("choice: ")
#
#     if choice == "a":
#         n1 = int(input('number 1: '))
#         n2 = int(input('number 2: '))
#         print("sum is",add(n1,n2))
#     if choice == "s":
#         n1 = int(input('number 1: '))
#         n2 = int(input('number 2: '))
#         print("sub is", sub(n1, n2))
#     if choice == "m":
#         n1 = int(input('number 1: '))
#         n2 = int(input('number 2: '))
#         print("mul is", mul(n1, n2))
#     if choice == "d":
#         n1 = int(input('number 1: '))
#         n2 = int(input('number 2: '))
#         print("div is", div(n1, n2))
#     if choice == "x":
#         print("thank you")
#         break


# display_list = [(1920, 1080, 5000),
#                 (1280, 720, 3000),
#                 (1024, 768, 2000),
#                 (640, 480, 500),
#                 (1280, 720, 400)]
# a = []
# for i in range(len(display_list)):
#     a.append(display_list[i][2])
# b = min(a)
# print(b)
# for k in range(len(display_list)):
#     if display_list[k][2] == b:
#         print('horizontal',display_list[k][0],",",'vertical',display_list[k][1])


# myFruits = ("apple", "banana", "cherry")
# myFruits[1] = 'mango'
# myFruits.add('apple')
# print(myFruits)

# fruits = {"apple", "banana", "cherry", "apple", "pine-apple", 34.21}
# print('Values: ', fruits)
# print('size: ', len(fruits))
# print()
# myDrinks = ['tea', 'coffee', 'banana', 'water']
# fruits.update(myDrinks)
# print('After merging: ', fruits)
# print('size: ', len(fruits))
#
# def getName():
#     name = input('Name: ')
#     return name
# def getAge():
#     age = int(input('Age: '))
#     return age
# def printAllInfo(*allInfo):
#     for info in allInfo:
#         print(info)
# def evaluateMark(marks=0,name='no name'):
#     if(marks > 90):
#         print(f'{name} got A')
#     else:
#         print('Not a good grade')
# def getMarkOfCSC101():
#     mark = int(input())
#     return mark
# studentName = getName()
# studentAge = getAge()
# studentmark = getMarkOfCSC101()
# printAllInfo(studentName, studentAge)
#
# evaluateMark(studentmark, name = studentName)


def pyramid(lines):
    for i in range(lines):
        for j in range(i+1):
            print(i+1, end='')
        print()
x = int(input('Lines: '))
pyramid(x)