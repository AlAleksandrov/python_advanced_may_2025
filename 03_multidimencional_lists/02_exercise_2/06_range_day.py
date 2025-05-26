SIZE = 5

matrix =[]
my_place = [0, 0]
targets = 0

for row in range(SIZE):
    matrix.append(list(input().split()))
    for col in range(SIZE):
        if matrix[row][col] == "A":
            my_place = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}
targets_down = []

for _ in range(int(input())):
    commands = input().split()
    if commands[0] == "move":
        coordinates = directions[commands[1]]
        new_row = my_place[0] + coordinates[0] * int(commands[2])
        new_col = my_place[1] + coordinates[1] * int(commands[2])
        if 0 <= new_row < SIZE and 0 <= new_col < SIZE and matrix[new_row][new_col] == ".":
            matrix[new_row][new_col] = "A"
            matrix[my_place[0]][my_place[1]] = "."
            my_place = [new_row, new_col]
    elif commands[0] == "shoot":
        coordinates = directions[commands[1]]
        new_row = my_place[0] + coordinates[0]
        new_col = my_place[1] + coordinates[1]
        while 0 <= new_row < SIZE and 0 <= new_col < SIZE:
            if matrix[new_row][new_col] == "x":
                targets -= 1
                targets_down.append([new_row, new_col])
                matrix[new_row][new_col] = "."
                break
            new_row += directions[commands[1]][0]
            new_col += directions[commands[1]][1]

        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break


if targets > 0:
    print(f"Training not completed! {targets} targets left.")
[print(row) for row in targets_down]