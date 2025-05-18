from collections import deque


quantity = int(input())
queue = deque()
names = input()

while names != "Start":
    queue.append(names)
    names = input()


command = input()

while command != "End":
    if command.isdigit():
        if quantity >= int(command):
            print(f"{queue.popleft()} got water" )
            quantity -= int(command)
        else:
            print(f"{queue.popleft()} must wait")
    elif command.startswith("refill"):
        quantity += int(command.split()[1])

    command = input()

print(f"{quantity} liters left")