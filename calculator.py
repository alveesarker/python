n = int(input("Enter your number:"))
i = 1
oss = 0
ess = 0
while i <= n:
    if(i % 2 != 0):
        oss += i*i
    else:ess += i*i
    i += 1
i = 0
while i <= n:
    print(f'{i}x{i}+', end='')
    i += 2
print(f'= {ess}')
i = 1
while i <= n:
    print(f'{i}x{i}+', end='')
    i += 2
print(f'= {oss}')

i, j, k = 8, 5, 7
if k > j and k > i:
    k = j + i
elif k > j:
    if k < i:
        k = i
    else:k = j
if i % 2 != 0:
    i -= 1
elif(j + k)%2 == 0:
    i = j + k
j = (i+k)//j
print(i,j,k)

n = int(input('enter your number:'))
i = 1
s = 0
while i <= n:
    if i % 2 != 0:
        s += i * i
        print(f'{i}^2+', end='')
    i += 1
print(f'={s}')

x = 'hello dear students!'
print(x[-10:-1])


i, j, k = 3, 5, 7
if i<j:
    if j<k:
        i +=j
    else:
        j = k
elif i%j == 0:
    if j<k:
        i-=k
    else:
        j-=k
else:
    if j>k:
        j = i
    else:
        i = k
print(i, j, k)
#

Mark = float(input('Enter Mark:'))
if Mark >= 90 and Mark <=100:
   print(f'{Mark} -> A')
elif Mark >= 85 and Mark <90:
   print(f'{Mark} -> A-')
elif Mark >= 80 and Mark < 85:
   print(f'{Mark}-> B+')
else:
   print(f'{Mark}-> Fail')


name = str(input('Enter your name:'))
id = int(input('Enter your id:'))
cgpa = float(input('Enter your cgpa:'))
if cgpa >= 3.50 and cgpa <= 4.00:
    print(f'Dear Student {name} with {id}. Your CGPA is {cgpa} and you received Distinction in your graduation.')

a = int(input('Price of item 1:'))
b = int(input('Price of item 2:'))
c = int(input('Price of item 3:'))
if a < b:
    if b < c:
        minimum = a

num1 = int(input("Price of item 1:"))
num2 = int(input("Price of item 2:"))
num3 = int(input("Price of item 3:"))
#
discount = min(num1, num2, num3)
total = num1 + num2 + num3
payable = total - discount
#
print("Total:", total)
print(f'Discount:', discount)
print(f'Payable amount::', payable)


#if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('yes')
        else:print('no')
    else: print('yes')
else:print('no')

n = int(input('Enter:'))
i = 1
s = 0
while i <= n:
    if i == 1:
        print(f'{i}+', end='')
    elif i == n:
        print(f'1/{i}', end='')
    else:print(f'1/{i}+', end='')
#
    s += 1/i
    i += 1
print(f'={s:.4f}')


num1 = int(input("Price of item 1:"))
num2 = int(input("Price of item 2:"))
num3 = int(input("Price of item 3:"))
minimum = min(num1, num2, num3)
maximum = max(num1, num2, num3)
total = num1 + num2 + num3
middle = total - minimum - maximum
print(minimum, middle, maximum)

#enter a number between 0 to 50 and prime number:
n = int(input('Enter a number (between 0 and 50):'))
while n < 0 or n >50:
    print('Number out of range! Enter number between 0 and 50')
    n = int(input('Enter a number (between 0 and 50):'))
if n > 1:
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i) == 0:
            print(f"{n} is not a prime number.")
            break
    else:
        print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")


thought game
T = int(input())
for __ in range(T):
#
    X, Y = map(int, input().split())
    average = (X + Y) // 2
    if average % 2 == 0:
        print("Sadia will be happy.")
    else:
        print("Oops!")


A, B = map(int, input().split())
hateache = 0
confused = "No"
while A > 0 or B > 0:
    digit_sum = (A % 10) + (B % 10) + carry
    hateache = digit_sum // 10
    if hateache == 1:
        confused = "Yes"
        break
    A //= 10
    B //= 10
print(confused)

n = int(input())
a=0
b=1
for i in range(2, n+1):
  c=a+b
  a=b
  b=c
print(b)


A = input()
p = A[0].upper() + A[1:]
p = p.replace('s', '$')
p = p.replace('i', '!')
p = p.replace('o', '()')
p = p +'.'
print(p)

