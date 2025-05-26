n = int(input())

matrix =[]
alice_place = [0, 0]

for row in range(n):
    matrix.append(list(input().split()))
    for col in range(n):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            alice_place = [row, col]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}
tea_bags = 0

while tea_bags < 10:
    command = input()
    coordinates = directions[command]
    new_row = alice_place[0] + coordinates[0]
    new_col = alice_place[1] + coordinates[1]
    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
        break
    if matrix[new_row][new_col] == "R":
        matrix[new_row][new_col] = "*"
        break

    if matrix[new_row][new_col] not in "*.":
        tea_bags += int(matrix[new_row][new_col])

    alice_place = [new_row, new_col]
    matrix[new_row][new_col] = "*"

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*row) for row in matrix]