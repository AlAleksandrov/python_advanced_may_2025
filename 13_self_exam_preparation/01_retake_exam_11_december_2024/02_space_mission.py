n = int(input())

grid = []
my_place = [0, 0]

resources = 100

for rows in range(n):
    grid.append(list(input().split()))
    for cols in range(n):
        if grid[rows][cols] == "S":
            my_place = [rows, cols]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    command = input()
    coordinates = directions[command]
    new_row = my_place[0] + coordinates[0]
    new_col = my_place[1] + coordinates[1]

    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
        print("Mission failed! The spaceship was lost in space.")
        break

    resources -= 5
    if grid[my_place[0]][my_place[1]] != "R":
        grid[my_place[0]][my_place[1]] = "."

    my_place = [new_row, new_col]

    if grid[new_row][new_col] == ".":
        grid[new_row][new_col] = "S"

    elif grid[new_row][new_col] == "M":
        resources -= 5
        grid[new_row][new_col] = "S"

    elif grid[new_row][new_col] == "R":
        resources += 10
        if resources > 100:
            resources = 100

    elif grid[new_row][new_col] == "P":
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        break

    if resources < 5:
        print("Mission failed! The spaceship was stranded in space.")
        break


[print(*row) for row in grid]