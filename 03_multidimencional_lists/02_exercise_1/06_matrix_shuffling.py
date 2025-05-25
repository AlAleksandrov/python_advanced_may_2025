rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

while True:
    commands = input().split()
    if commands[0] == "END":
        break

    if commands[0] != "swap" or len(commands) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in commands[1:]]
    if 0 <= row1 < rows and 0 <= row2 < rows and 0 <= col1 < cols and 0 <= col2 < cols:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")