n = int(input())

matrix = []
my_place = [0, 0]
star_collection = 2

for rows in range(n):
    matrix.append(list(input().split()))
    for cols in range(n):
        if matrix[rows][cols] == "P":
            my_place = [rows, cols]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

while True:
    if star_collection == 10:
        break

    if star_collection == 0:
        break

    command = input()
    coordinates = directions[command]
    new_row = my_place[0] + coordinates[0]
    new_col = my_place[1] + coordinates[1]

    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
        matrix[my_place[0]][my_place[1]] = "."
        my_place = [0, 0]
        if matrix[my_place[0]][my_place[1]] == "*":
            star_collection += 1
        matrix[my_place[0]][my_place[1]] = "P"
        continue

    elif matrix[new_row][new_col] == "#":
        star_collection -= 1
        continue

    matrix[my_place[0]][my_place[1]] = "."

    if matrix[new_row][new_col] == "*":
        star_collection += 1

    my_place = [new_row, new_col]
    matrix[my_place[0]][my_place[1]] = "P"


if star_collection == 10:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is [{my_place[0]}, {my_place[1]}]")
[print(*row) for row in matrix]