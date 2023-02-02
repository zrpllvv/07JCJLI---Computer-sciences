import numpy as np
file = open("input.txt", "r")
table = []
for line in file:
    temperatures = line.strip().split(" ")
    intTemp = []
    for temp in temperatures:
        intTemp.append(int(temp))
    table.append(intTemp)
file.close()

def max_function (l, k, matrix1):
    value = True
    max1 = matrix1[l][k]
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i == 0 and j == 0:
                value = True
            else:
                if max1 <= matrix1[l + i][k + j]:
                    return False
    return value

n = len(table)
m = len(table[0])

matrix = np.array([[0 for j in range(m + 4)] for i in range(n + 4)])

for i in range(n):
    for j in range(m):
        matrix[i + 2][j + 2] = table[i][j]

answer = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if max_function(i+2, j+2, matrix) == True:
            answer[i][j] = table[i][j]
        else:
            answer[i][j] = '-'

def print_matrix(matrix2):
     for row in matrix2:
         print('\t'.join(str(x) for x in row))

print_matrix(answer)










