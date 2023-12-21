b = list(str(input()))

i = -3
while i > -len(b):
    b.insert(i, ",")
    i += -4

for i in b:
    print(i, end='')


A = int(input())
print(format(A,","))

n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print(" ".join("*" * i))





l = 'abcdefghijklmnopqrstuvwxyz '
n = int(input())
word = input()
p = word
for i in range(len(word)):
    if l[l.index(word[i])] == " ":
        p = p.replace(l[l.index(word[i])], l[l.index(word[i])])
    else:
        if word[i] == "a" and "b":
            p = p.replace(l[l.index(word[i])], l[l.index(word[i]) - 3])
        else:
            p = p.replace(l[l.index(word[i])], l[l.index(word[i]) - 2])
print(p)

test = int(input())

for i in range(test):
    over = [*(input())]
    balls = 0
    for i in range(len(over)):
        if over[i] != "W" and over[i] != "N" and over[i] != "D":
            balls = balls + 1

    if balls > 6 and balls % 6 != 0:
        o_ver = str(balls // 6)
        b_all = str(balls % 6)
        if int(o_ver) > 1:
            st_over = " OVERS "
        else:
            st_over = " OVER "
        if int(b_all) > 1:
            st_ball = " BALLS"
        else:
            st_ball = " BALL"
        print(o_ver + st_over + b_all + st_ball)
    elif balls % 6 == 0:
        o_ver = str(balls // 6)
        if int(o_ver) > 1:
            st_over = " OVERS"
        else:
            st_over = " OVER"
        print(o_ver + st_over)
    else:
        b_all = str(balls % 6)
        if int(b_all) > 1:
            st_ball = " BALLS"
        else:
            st_ball = "BALL"
        print(b_all + st_ball)


a, n = map(int, input().split())
b = [0,1,2]
i = 0
while len(b) <= 50:
    b.append(b[-1]+b[-2])
    if a <= b[i] <= n:
        print(b[i])
    i += 1


a = [0, 1, 2]
while len(a) < 41: a += [sum(a[-2:])]
x, y = map(int, input().split())
[print(i) for i in a if x <= i <= y]

n = int(input())
i = 1
n = int(input())
for i in range(n):
    for j in range(n):
        if j > n-i :
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

n = int(input())
b = []
for i in range(n):
    b.append(f'{" ".join("*"*(i+1))}')
for i in range(len(b)):
    print(f'{" "*(len(b)-1-i)}{b[i]}')
print(b)


R, C = map(int, input().split())
grid = [input() for i in range(R)]
count = 0

for i in range(R):
    for j in range(C):
        print(grid)
        if grid[i][j] == "*":
            continue

        star = 0
        if i != 0 and grid[i - 1][j] == "*":
            star += 1
        if i != R - 1 and grid[i + 1][j] == "*":
            star += 1
        if j != 0 and grid[i][j - 1] == "*":
            star += 1
        if j != C - 1 and grid[i][j + 1] == "*":
            star += 1

        if star == 0:
            count += 1

print(count)


A11, A12 = map(int, input().split())
A21, A22 = map(int, input().split())
B11, B12 = map(int, input().split())
B21, B22 = map(int, input().split())

C11 = A11 * B11 + A12 * B21
C12 = A11 * B12 + A12 * B22
C21 = A21 * B11 + A22 * B21
C22 = A21 * B12 + A22 * B22

print(C11, C12)
print(C21, C22)

a = int(input('enter row:'))
matA = [[int(j) for j in input('matA:').split()]for i in range(a)]
b = int(input('enter row:'))
matB = [[int(j) for j in input('matB:').split()]for i in range(b)]

def multiply(matA, matB):
      if len(matA[0]) != len(matB):
          print('it is not possible')
      else:
          result =[[0 for j in range(len(matB[0]))]for i in range(len(matA))]
          for r in range(len(result)):
              for c in range(len(result[r])):
                  s = 0
                  for i in range(len(matA)):
                      cal = matA[r][i] * matB[i][c]
                      s += cal
                  result[r][c] = s
          return result
result = multiply(matA,matB)
print(*result,sep='\n')



#MINE
r, c = map(int, input().split())
grid = []
for i in range(r):
    row = input()
    grid.append(list(row))

for i in range(r):
    for j in range(c):
        if grid[i][j] == '.':
            mines = 0
            if i > 0 and j > 0 and grid[i-1][j-1] == '*':
                mines += 1
            if i > 0 and grid[i-1][j] == '*':
                mines += 1
            if i > 0 and j + 1 < c and grid[i-1][j+1] == '*':
                mines += 1
            if j > 0 and grid[i][j-1] == '*':
                mines += 1
            if j + 1 < c and grid[i][j+1] == '*':
                mines += 1
            if i + 1 < r and j > 0 and grid[i+1][j-1] == '*':
                mines += 1
            if i + 1 < r and grid[i+1][j] == '*':
                mines += 1
            if i + 1 < r and j + 1 < c and grid[i+1][j+1] == '*':
                mines += 1

            if mines != 0:
                grid[i][j] = str(mines)

        print(grid[i][j], end='')
    print()


#Incompatible Crops
r, c = map(int, input().split())
grid = []
count = 0
for i in range(r):
    row = input()
    grid.append(list(row))
for i in range(r):
    for j in range(c):
        if grid[i][j] == ".":
            mine= 0

            if j != 0 and grid[i][j - 1] == '*':
                mine += 1
            if j != c-1 and grid[i][j + 1] == '*':
                mine += 1
            if i != 0 and grid[i - 1][j] == '*':
                mine += 1
            if i != r-1 and grid[i + 1][j] == '*':
                mine += 1
            if mine == 0:
                count += 1
print(count)


#CASH CHANGE
N = int(input())
moneynote = [1, 5, 10, 50, 100, 500]
tk = []

for d in reversed(moneynote):
    while N >= d:
        tk.append(d)
        N -= d

notes = tk[::-1]
print(" ".join(map(str, notes)))5


#LITTLE SUBARRAY SUM
def subarray_sum(list, a, b):
    sum = 0
    list = numbers[a:b + 1]
    for i in list:
        sum = sum + i
    return sum

N, A, B = map(int, input().split())
numbers = list(map(int, input().split()))
#
t = subarray_sum(numbers, A, B)
print(t)

#SET UNION
n, m = map(int, input().split())

set1 = list(map(int, input().split()))
set2 = list(map(int, input().split()))
set1.extend(set2)

union = []

for i in set1:
    if i not in union:
        union.append(i)

union.sort()
print(*union)



#GOAT RESEARCH
n = int(input())
grid = []
for i in range(n):
    row = input()
    grid.append(list(row))

for j in range(n):
    if len(grid[j]) == 2:
        grid[j].append('a')
    if len(grid[j]) % 2 == 0:
        grid[j].pop(-1)
a = max(grid)
b = len(a)
for g in range(n):
    print(f"{' ' * int((b - len(grid[g])) / 2)}", end='')
    for d in range(len(grid[g])):
        print(grid[g][d], end='')
    print()


#Missing Number
a = int(input())
b = list(map(int, input().split()))
c = sum(b)
d = a - c
print(d)


#Mixed Fractions
a,b = map(int, input().split())
c = a // b
d = a % b
print(c, d, b)

#Math and Watermelons
a,b = map(int, input().split())
print(a % b)


Is Palindrome
a = list(input())
b = []
for i in range(-1, -(len(a))-1, -1):
    b.append(a[i])
if a == b:
    print('Yes')
else:
    print('No')



#Neat Brackets
a = list(input())
if len(a) % 2 == 0:
    if a[0] == ')' and a[-1] == '(':
        print('No')
    else:
        b = list(a[0:int(len(a)/2)])
        c = list(a[int(len(a)/2):])
        d =[]
        for i in range(len(c)):
            if c[i] == '(':
                x = c[i].replace('(',')')
                d.append(x)
            if c[i] == ')':
                y = c[i].replace(')','(')
                d.append(y)
        d.reverse()
        if b == d:
            print('Yes')
        else:
            print('No')
else:
    print('No')
