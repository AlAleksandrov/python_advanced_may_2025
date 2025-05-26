n = int(input())

matrix =[]
bunny_place = [0, 0]

for row in range(n):
    matrix.append(list(input().split()))
    for col in range(n):
        if matrix[row][col] == "B":
            bunny_place = [row, col]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}
max_eggs = -float("inf")
best_direction = ""
matrix_best_coordinates = []

for direction, coordinates in directions.items():
    eggs = 0
    new_bunny_place = []
    new_row = bunny_place[0] + coordinates[0]
    new_col = bunny_place[1] + coordinates[1]

    while 0 <= new_row < n and 0 <= new_col < n:
        if matrix[new_row][new_col] == "X":
            break

        eggs += int(matrix[new_row][new_col])
        new_bunny_place.append([new_row, new_col])
        new_row += coordinates[0]
        new_col += coordinates[1]

    if eggs > max_eggs and new_bunny_place:
        max_eggs = eggs
        best_direction = direction
        matrix_best_coordinates = new_bunny_place

print(best_direction)
[print(row) for row in matrix_best_coordinates]
print(max_eggs)