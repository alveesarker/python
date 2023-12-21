# n = int(input())
# s = 0
# i = 1
# while i <= n:
#     s = s + i
#     i += 1
# print(s)

# 1 Write a program in Python to display the first 10 natural numbers.
# start = 0
# end = 9
# while start <= end:
#     print(start)
#     start += 1

# 2Write a Python program to find the sum of first 10 natural numbers.
# n = 10
# s = 0
# i = 1
# while i <= n:
#     s += i
#     i += 1
# print(s)

# 3 Write a Python program to find the sum of series 1+3+5+7..+N.
# n = int(input("enter your number:"))
# s = 0
# i = 1
# while i <= n:
#     s += i
#     i += 1
# print(f"sum of the series:{s}")

# 4 Write a Python Program to find the sum of series 1^2+2^2+3^2...+N^2.
# n = int(input("enter your number:"))
# s = 0
# i = 1
# while i <= n:
#     s += i * i
#     i += 1
# print(f"sum of the series:{s}")


# 5 Write a Python Program to find the sum of series 1^1+2^2+3^3...+N^N

# n = int(input("enter your number:"))
# s = 0
# i = 1
# f = 1
# while i <= n:
#     s += i ** f
#     i += 1
#     f += 1
# print(f"sum of the series:{s}")

# 6 Write a Python program to display the multiplication table of a given integer.
# n = int(input("enter your number:"))
# s = 1
# i = 1
# while i <= 10:
#     s = i * n
#     print(f"{n} X {i} = {s}")
#     i += 1

# 7 Write a Python program to display the n terms of odd natural number and their sum.
# n = int(input("enter your number:"))
# s = 1
# i = 1
# odd = 2
# f = 0
# while i <= n:
#     i += 1
#     f += s
#     print(s)
#     s += odd
# print(f'sum of odd number:{f}')


# n = int(input("enter your number:"))
# s = 0
# i = 1
# a = 1
# while i <= n:
#     print(a)
#     s += a
#     a *= 3
#     i += 1
# print(f'sum of the number:{s}')


# 8 Write a Python program to display the cube of the number upto given an integer.
# n = int(input('enter your number:'))
# i = 1
# s = 0
# cube = 1
# while cube <= n:
#     s += cube
#     print(cube)
#     i += 1
#     cube = i **3
# print(f'sum of the cube:{s}')


# 9 Write a Python program to calculate the factorial of a given number.
# n = int(input("Enter your number:"))
# i = 1
# f = 1
# while i <= n:
#     f *= i
#     print(i , f)
#     i += 1
# print(f'factorial of the number is {f}')


# nCr = n! / (r! * (n-r)!)
# n, r = map(int, input().split())
# i = 1
# f = 1
# while i <= n:
#     f *= i
#     i += 1
# n_f = f
#
# i = 1
# f = 1
# while i <= r:
#     f *= i
#     i += 1
# r_f = f
#
# i = 1
# f = 1
# while i <= (n-r):
#     f *= i
#     i += 1
# n_r_f = f
#
# fac = n_f // (r_f * n_r_f)
# print(f"{n}C{r} = {fac}")


#nCr = n! / (r! * (n-r)!) with function
# def factorial(x):
#     i = 1
#     f = 1
#     while i <= x:
#         f *= i
#         i += 1
#     return f
# n, r = map(int, input().split())
# fac = factorial(n) // (factorial(r) * factorial(n-r))
# print(fac)


#average cgpa
# n = int(input("enter student number:"))
# i = 1
# s = 0
# while i <= n:
#     cgpa = (float(input(f'enter cgpa {i}:')))
#     i += 1
#     s += cgpa
# average = s / n
# print(average)


#minimum
# n = int(input())
# minimum = int(input())
# i = 2
# while i <= n:
#     a = int(input())
#     i += 1
#     if a < minimum:
#          minimum = a
# print("minimum", minimum)

#maximum cgpa
# n = int(input('Enter number of student;'))
# maximum = float(input())
# i = 2
# while i <= n:
#     a = float(input())
#     i += 1
#     if a > maximum:
#         maximum = a
# print("maximum", maximum)


#minimum maximum average
n = int(input('Enter number of students: '))
i = 1
minimum = 5.0
maximum = -1.0
#
s = 0
while i <= n:
    cgpa = float(input())

    if cgpa < minimum:
        minimum = cgpa

    if cgpa > maximum:
        maximum = cgpa

    s += cgpa
    i += 1

print(f'Minimum CGPA: {minimum:.2f}')
print(f'Maximum CGPA: {maximum:.2f}')
average = s / n
print(f'Average CGPA: {average:.2f}')

