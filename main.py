def my_angle(a, b):
    c2 = a * a + b * b
    c = c2 ** 0.5
    print(f'hypoteneous: {c}')
    return "hello"

my_angle(3,4)

def addition(a , b):
    result = a + b
    print(f'addition ({a} + {b}) = {result}')

def subtraction(a , b):
    result = a - b
    print(f'subtraction ({a} - {b}) = {result}')
a = int(input('enter number 1:'))
b = int(input('enter number 2:'))
addition(a , b)
subtraction(a ,b)

def multiplication(a , b):
    result = a * b
    print(f'multiplication ({a} x {b}) = {result} ')
def division(a , b):
    result = a / b
    print(f'division ({a} / {b}) = {result} ')
a = int(input('Enter num 1:'))
b = int(input('Enter num 2:'))
multiplication(a , b)
division(a , b)
def subtracion(a,b):
    result = a - b
    print(f"subtraction({a} - {b}) = {result}")
subtracion(15,14)


name = "alvee sarker"
idd = 2311249
print(f'Hello i am {name} and my id is {idd} ')
s = 345
i = 1
while i <= 9:
    print(f'{i}x{i}+', end='')
    i+=2
print(f'={s}')
for i in range(5):
    print(i)
