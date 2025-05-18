from collections import deque


petrol_pumps = int(input())
amount_of_petrol = deque()
distance = deque()
count = 0
stops = 0

for _ in range(petrol_pumps):
    information = input()
    amount_of_petrol.append(int(information.split()[0]))
    distance.append(int(information.split()[1]))

while stops < petrol_pumps:
    litres = 0
    km = 0
    for index in range(petrol_pumps):
        litres += amount_of_petrol[index]
        km = distance[index]
        if litres < km:
            amount_of_petrol.rotate(-1)
            distance.rotate(-1)
            stops = 0
            count += 1
            break
        litres -= km
        stops += 1


if count > 0:
    print(count)
else:
    print(0)