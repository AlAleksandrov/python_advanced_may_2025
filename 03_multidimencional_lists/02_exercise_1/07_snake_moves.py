from collections import deque


rows, cols = [int(x) for x in input().split()]

string = deque(input())

matrix = []

for row in range(rows):
    matrix.append([""] * cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = string[0]
        else:
            matrix[row][-col-1] = string[0]
        string.rotate(-1)


[print(*r, sep="") for r in matrix]