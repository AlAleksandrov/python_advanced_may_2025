from collections import deque


working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
honey_making = deque(input().split())
total_honey = 0

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else 0
}

while working_bees and nectar:
    if nectar[-1] >= working_bees[0]:
        total_honey += abs(operators[honey_making[0]](working_bees[0], nectar[-1]))
        working_bees.popleft()
        nectar.pop()
        honey_making.popleft()
    else:
        nectar.pop()


print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")