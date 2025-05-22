from collections import deque


string = [x for x in input().split()]

queue = deque()

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y if y != 0 else 0,
}


for char in string:
    if char not in ["+", "-", "*", "/"]:
        queue.append(int(char))
    else:
        while len(queue) > 1:
           result  = operators[char](queue[0], queue[1])
           queue.popleft()
           queue.popleft()
           queue.appendleft(result)


print(*queue)