from collections import deque


weight = [int(x) for x in input().split()]
courier = deque(int(x) for x in input().split())
total_weight = 0

while weight and courier:
    if courier[0] == weight[-1]:
        courier.popleft()
        total_weight += weight.pop()
    elif courier[0] > weight[-1]:
        courier[0] -= 2 * weight[-1]
        total_weight += weight.pop()
        if courier[0] > 0:
            courier.rotate(-1)
        else:
            courier.popleft()
    elif courier[0] < weight[-1]:
        weight[-1] -= courier[0]
        total_weight += courier.popleft()


print(f"Total weight: {total_weight} kg")
if not weight and not courier:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

elif weight and not courier:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: "
          f"{', '.join(str(x) for x in weight)}")

elif courier and not weight:
    print(f"Couriers are still on duty: "
          f"{', '.join(str(x) for x in courier)} but there are no more packages to deliver.")