from collections import deque


bee = deque(int(x) for x in input().split())
bee_eaters = [int(x) for x in input().split()]

while bee and bee_eaters:
    if bee[0] >= 7 * bee_eaters[-1]:
        bee[0] -= 7 * bee_eaters[-1]
        bee.rotate(-1)
        bee_eaters.pop()
        if bee[-1] == 0:
            bee.pop()
    else:
        bee_eaters[-1] -= bee[0] // 7
        bee.popleft()


print("The final battle is over!")
if not bee and not bee_eaters:
    print("But no one made it out alive!")
elif bee:
    print(f"Bee groups left: {', '.join(str(x) for x in bee)}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eaters)}")