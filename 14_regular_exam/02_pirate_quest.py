n = int(input())

matrix = []
pirate_ship_place = []
durability = 100
treasure = 0

for i in range(n):
    row = list(input())
    if "S" in row:
        pirate_ship_place = [i, row.index("S")]
    if "*" in row:
        treasure += row.count("*")
    matrix.append(row)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

is_charm = False

while True:
    command = input()

    if durability == 0:
        print(f"Shipwreck! Last known coordinates ({pirate_ship_place[0]}, {pirate_ship_place[1]})")
        break

    if treasure == 0:
        print("Yo-ho-ho! All treasure chests collected!")
        break

    if command == "stop":
        print("Retreat! Some treasures remain unclaimed.")
        break

    row, col = directions[command]
    new_row = (row + pirate_ship_place[0]) % n
    new_col = (col + pirate_ship_place[1]) % n

    matrix[pirate_ship_place[0]][pirate_ship_place[1]] = "."
    pirate_ship_place = [new_row, new_col]

    if matrix[new_row][new_col] == "*":
        matrix[new_row][new_col] = "."
        treasure -= 1
    elif matrix[new_row][new_col] == "C" and not is_charm:
        matrix[new_row][new_col] = "."
        durability += 25
        is_charm = True
        if durability > 100:
            durability = 100
    elif matrix[new_row][new_col] == "M":
        matrix[new_row][new_col] = "."
        durability -= 25

    matrix[pirate_ship_place[0]][pirate_ship_place[1]] = "S"


print(f"Ship Durability: {durability}")

if treasure > 0:
    print(f"Unclaimed chests: {treasure}")

for row in matrix:
        print("".join(row))