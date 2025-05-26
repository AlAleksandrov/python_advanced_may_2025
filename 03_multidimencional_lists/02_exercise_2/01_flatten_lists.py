strings = input().split("|")

matrix = []

for string in strings[::-1]:
    row = string.split()
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, end=" ")