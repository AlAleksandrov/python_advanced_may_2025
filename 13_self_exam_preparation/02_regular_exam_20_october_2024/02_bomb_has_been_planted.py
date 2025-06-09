n, m = map(int,input().split(", "))

matrix = []
counter_terrorist_place = [0, 0]
complete_time = 16
is_for_defuse = False

for rows in range(n):
    matrix.append(list(input()))
    for cols in range(m):
        if matrix[rows][cols] == "C":
            counter_terrorist_place = [rows, cols]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
    "defuse": [0, 0]
}

while True:
    if complete_time > 0:
        command = input()
        coordinates = directions[command]
        new_row = counter_terrorist_place[0] + coordinates[0]
        new_col = counter_terrorist_place[1] + coordinates[1]

        if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
            complete_time -= 1
            continue

        counter_terrorist_place = [new_row, new_col]

        if command != "defuse":
            is_for_defuse = False

            if matrix[new_row][new_col] == "B":
                is_for_defuse = True
            elif matrix[new_row][new_col] == "T":
                matrix[new_row][new_col] = "*"
                print("Terrorists win!")
                break

            complete_time -= 1

        else:
            if is_for_defuse:
                if complete_time >= 4:
                    complete_time -= 4
                    matrix[new_row][new_col] = "D"
                    print(f"Counter-terrorist wins!\nBomb has been defused: {complete_time} second/s remaining.")
                    break

                else:
                    matrix[new_row][new_col] = "X"
                    print(f"Terrorists win!\nBomb was not defused successfully!\nTime needed: {4 - complete_time} second/s.")
                    break

            else:
                complete_time -= 2
                continue
    else:
        print(f"Terrorists win!\nBomb was not defused successfully!\nTime needed: 0 second/s.")
        break

for row in matrix:
        print("".join(row))