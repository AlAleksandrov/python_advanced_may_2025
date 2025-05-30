presents =int(input())
size = int(input())

matrix = []
santa = [0, 0]
nice_kids = 0

for row in range(size):
    matrix.append(list(input().split()))
    for col in range(size):
        if matrix[row][col] == "S":
            santa = [row, col]
        if matrix[row][col] == "V":
            nice_kids += 1

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}
count_down_nice_kids = nice_kids

while True:
    if presents == 0:
        # matrix[santa[0]][santa[1]] = "S"
        print("Santa ran out of presents!" if count_down_nice_kids != 0 else "")
        break

    command = input()

    if command == "Christmas morning":
        # matrix[santa[0]][santa[1]] = "S"
        break

    coordinates = directions[command]
    new_row = santa[0] + coordinates[0]
    new_col = santa[1] + coordinates[1]
    if 0 <= new_row < size and 0 <= new_col < size:

        if matrix[new_row][new_col] == "X":
            matrix[new_row][new_col] = "S"
            matrix[santa[0]][santa[1]] ="-"
            santa = [new_row, new_col]
        elif matrix[new_row][new_col] == "V":
            presents -= 1
            matrix[new_row][new_col] = "S"
            count_down_nice_kids -= 1
            matrix[santa[0]][santa[1]] = "-"
            santa = [new_row, new_col]
        elif matrix[new_row][new_col] == "C":
            matrix[santa[0]][santa[1]] = "-"
            santa = [new_row, new_col]
            matrix[new_row][new_col] = "S"
            for move, values in directions.items():
                new_r = santa[0] + values[0]
                new_c = santa[1] + values[1]
                if matrix[new_r][new_c] in "X":
                    presents -= 1
                    matrix[new_r][new_c] = "-"
                if matrix[new_r][new_c] == "V":
                    presents -= 1
                    matrix[new_r][new_c] = "-"
                    count_down_nice_kids -= 1
        else:
            matrix[santa[0]][santa[1]] = "-"
            santa = [new_row, new_col]


[print(*row) for row in matrix]
if count_down_nice_kids == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {count_down_nice_kids} nice kid/s.")