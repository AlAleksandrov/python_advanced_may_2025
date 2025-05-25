rows, cols = [int(x) for x in input().split()]

for row in range(rows):
    for col in range(cols):
        print(chr(ord("a") + row) + chr(ord("a") + row + col) + chr(ord("a") + row), end=" ")
    print()