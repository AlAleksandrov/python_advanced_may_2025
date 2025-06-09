from collections import deque


strength_values = [int(x) for x in input().split()]
accuracy_values = deque(int(x) for x in input().split())
scored_goals = 0

while strength_values and accuracy_values:
    summarize = strength_values[-1] + accuracy_values[0]
    if summarize == 100:
        strength_values.pop()
        accuracy_values.popleft()
        scored_goals += 1
    elif summarize < 100:
        if strength_values[-1] < accuracy_values[0]:
            strength_values.pop()
        elif strength_values[-1] > accuracy_values[0]:
            accuracy_values.popleft()
        elif strength_values[-1] == accuracy_values[0]:
            strength_values[-1] = summarize
            accuracy_values.popleft()
    elif summarize > 100:
        strength_values[-1] = strength_values[-1] - 10
        accuracy_values.rotate(-1)


if scored_goals == 3:
    print(f"Paul scored a hat-trick!\nGoals scored: {scored_goals}")
elif scored_goals > 3:
    print(f"Paul performed remarkably well!\nGoals scored: {scored_goals}")
elif 0 < scored_goals < 3:
    print(f"Paul failed to make a hat-trick.\nGoals scored: {scored_goals}")
else:
    print("Paul failed to score a single goal.")

if strength_values:
    print(f"Strength values left: {', '.join(str(x) for x in strength_values)}")

if accuracy_values:
    print(f"Accuracy values left: {', '.join(str(x) for x in accuracy_values)}")