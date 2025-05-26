n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    commands = input().split()
    if commands[0] == "END":
        break

    if commands[0] == "Add":
        row, col, value = [int(x) for x in commands[1:]]
        if 0 <= row < len(matrix[0]) and 0 <= col < len(matrix[0]):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif commands[0] == "Subtract":
        row, col, value = [int(x) for x in commands[1:]]
        if 0 <= row < len(matrix[0]) and 0 <= col < len(matrix[0]):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

[print(*row) for row in matrix]