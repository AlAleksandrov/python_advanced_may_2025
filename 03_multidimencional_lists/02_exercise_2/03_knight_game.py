n = int(input())

matrix = []
knights =[]
possible_moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "K":
            knights.append([row, col])

removed_knights = 0

while True:
    best_hits = 0
    best_knight = [0, 0]

    for knight in knights:
        hits = 0
        for move in possible_moves:
            new_row = knight[0] + move[0]
            new_col = knight[1] + move[1]
            if 0 <= new_row < n and 0 <= new_col < n:
                if matrix[new_row][new_col] == "K":
                    hits += 1

        if hits > best_hits:
            best_hits = hits
            best_knight = [knight[0], knight[1]]

    if best_hits == 0:
        break

    knights.remove(best_knight)
    matrix[best_knight[0]][best_knight[1]] = "0"
    removed_knights += 1


print(removed_knights)