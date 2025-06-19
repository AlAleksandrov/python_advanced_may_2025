n = int(input())

matrix = []
traveler_place = [0, 0]
health = 100

for i in range(n):
    row_data = list(input())
    if "P" in row_data:
        traveler_place = [i, row_data.index("P")]
    matrix.append(row_data)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

while True:
    command = input()
    row, col = directions[command]
    new_row = row + traveler_place[0]
    new_col = col + traveler_place[1]

    if not 0 <= new_row < n or  not 0 <= new_col < n:
        continue

    matrix[traveler_place[0]][traveler_place[1]] = "-"
    traveler_place = [new_row, new_col]

    if matrix[new_row][new_col] == "M":
        health -= 40
        if health > 0:
            matrix[new_row][new_col] = "-"
        else:
            health = 0
            matrix[new_row][new_col] = "P"
            break

    elif matrix[new_row][new_col] == "H":
        health += 15
        matrix[new_row][new_col] = "-"
        if health > 100:
            health = 100

    elif matrix[new_row][new_col] == "X":
        matrix[new_row][new_col] = "P"
        break


if health == 0:
    print(f"Player is dead. Maze over!\nPlayer's health: {health} units")
else:
    print(f"Player escaped the maze. Danger passed!\nPlayer's health: {health} units")

for row in matrix:
        print("".join(row))