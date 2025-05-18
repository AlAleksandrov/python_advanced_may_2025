from collections import deque

quantity_of_food = int(input())
queue_of_orders = deque(map(int, input().split()))
order = 0

print(f"{max(queue_of_orders)}")

while queue_of_orders:
    if queue_of_orders[order] > quantity_of_food:
        break
    else:
        quantity_of_food -= queue_of_orders[order]
        queue_of_orders.popleft()

if queue_of_orders:
    print(f"Orders left: {' '.join(map(str, queue_of_orders))}")
else:
    print("Orders complete")