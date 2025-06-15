n = int(input())

matrix = []
my_bee_place = [0, 0]
energy = 15

for rows in range(n):
    matrix.append(list(input()))
    for cols in range(n):
        if matrix[rows][cols] == "B":
            my_bee_place = [rows, cols]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

amount_of_nectar = 0
MAKE_HONEY = 30
is_used = False

while True:
    if energy > 0:
        command = input()
        coordinates = directions[command]
        new_row = my_bee_place[0] + coordinates[0] # new_row = (my_bee_place[0] + coordinates[0]) % n !!! formula for row movement
        new_col = my_bee_place[1] + coordinates[1] # new_col = (my_bee_place[1] + coordinates[1]) % n !!! formula for col movement

        energy -= 1
        matrix[my_bee_place[0]][my_bee_place[1]] = "-"
        my_bee_place = [new_row, new_col]

        if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:

            if command == "left":
                my_bee_place = [new_row, new_col + n]

            elif command == "right":
                my_bee_place = [new_row, new_col - n]

            elif command == "up":
                my_bee_place = [new_row + n, new_col]

            elif command == "down":
                my_bee_place = [new_row - n, new_col]

        if matrix[my_bee_place[0]][my_bee_place[1]] == "H":
            matrix[my_bee_place[0]][my_bee_place[1]] = "B"
            if amount_of_nectar >= MAKE_HONEY:
                print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
            else:
                print("Beesy did not manage to collect enough nectar.")
            break

        elif matrix[my_bee_place[0]][my_bee_place[1]] != "-":
                amount_of_nectar += int(matrix[my_bee_place[0]][my_bee_place[1]])

        matrix[my_bee_place[0]][my_bee_place[1]] = "B"



    else:
        if amount_of_nectar < MAKE_HONEY:
            print("This is the end! Beesy ran out of energy.")
            break

        else:
            if is_used:
                print("This is the end! Beesy ran out of energy.")
                break
            else:
                energy += amount_of_nectar - MAKE_HONEY
                amount_of_nectar = MAKE_HONEY
                is_used = True


for row in matrix:
        print("".join(row))