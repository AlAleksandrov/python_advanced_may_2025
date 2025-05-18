from collections import deque

queue_names = deque(input().split())
number = int(input())


while len(queue_names) != 1:
    queue_names.rotate(-(number - 1))
    print(f"Removed {queue_names.popleft()}")


print(f"Last is {queue_names.pop()}")