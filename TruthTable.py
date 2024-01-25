#Generates a truth table grid based on the number of input columns
def table_maker(column):
    grid = []
    row = (2 ** column)
    for i in range(row):
        grid.append([])
    x = 2
    y = 1
    for k in range(column):
        for i in range(x):
            for j in range(int(y), int((row / x) + y)):
                if i % 2 == 0:
                    grid[j - 1].append('True')
                else:
                    grid[j - 1].append('False')
            y = y + (row / x)
        y = 1
        x *= 2

    return grid


#Generates a truth table for the AND operation
def table_for_and(column):
    truthTableList = table_maker(column)
    for i in range(len(truthTableList)):
        if i == 0:
            truthTableList[i].append('True')
        else:
            truthTableList[i].append('False')
    return truthTableList


#Generates a truth table for the OR operation
def table_for_or(column):
    truthTableList = table_maker(column)
    for i in range(len(truthTableList)):
        if i == len(truthTableList) - 1:
            truthTableList[i].append('False')
        else:
            truthTableList[i].append('True')
    return truthTableList



#Generates a truth table for the XOR operation
def table_for_xor(column):
    truthTableList = table_maker(column)
    for i in truthTableList:
        True_count = i.count('True')

        if True_count % 2 == 0:
            i.append('False')
        else:
            i.append('True')
    return truthTableList


def selectOperation(column):
    option = input('Enter operation(AND, OR, XOR, etc.): ')
    if option == 'AND' or option == 'and':
        truthTableList = table_for_and(column)
        return truthTableList
    elif option == 'OR'or option == 'or':
        truthTableList = table_for_or(column)
        return truthTableList
    elif option == 'XOR' or option == 'xor':
        truthTableList = table_for_xor(column)
        return truthTableList

column = int(input('Enter the number of variables: '))
truthTableList = selectOperation(column)
for i in range(len(truthTableList)):
    for j in range(len(truthTableList[i])):
        if j == len(truthTableList[i]) - 1:
            print(truthTableList[i][j], end='')

        elif j == len(truthTableList[i]) - 2:
            if truthTableList[i][j] == 'False':
                print(truthTableList[i][j], end='  |        ')
            else:
                print(truthTableList[i][j], end='   |        ')

        elif truthTableList[i][j] == 'True':
            print(truthTableList[i][j], end='   |   ')

        elif truthTableList[i][j] == 'False':
            print(truthTableList[i][j], end='  |   ')
    print()
    print('-----------' * column, '  ---------')


