from collections import deque


contestants = deque([int(x) for x in input().split()])
pieces_pie = [int(x) for x in input().split()]

while contestants and pieces_pie:
    contestant = contestants.popleft()
    pie = pieces_pie.pop()
    if contestant > pie:
        contestants.append(contestant - pie)
    elif contestant < pie:
        if len(pieces_pie) == 0:
            pieces_pie.append(pie - contestant)
        else:
            if pie - contestant > 1:
                pieces_pie.append(pie - contestant)
            elif pie - contestant == 1:
                pieces_pie[-1] += 1


if not pieces_pie and contestants:
    print(f"We will have to wait for more pies to be baked!\nContestants left: {', '.join(str(x) for x in contestants)}")
elif pieces_pie and not contestants:
    print(f"Our contestants need to rest!\nPies left: {', '.join(str(x) for x in pieces_pie)}")
else:
    print("We have a champion!")