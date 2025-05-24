from collections import deque


substrings = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ["red", "yellow"], "purple": ["red", "blue"], "green": ["yellow", "blue"]}
collected_colors =[]

while substrings:
    string = ""
    if len(substrings) > 1:
        if substrings[0] + substrings[-1] in main_colors + list(secondary_colors.keys()):
            string = substrings[0] + substrings[-1]
        elif substrings[-1] + substrings[0] in main_colors + list(secondary_colors.keys()):
            string = substrings[-1] + substrings[0]
        if string:
            substrings.pop()
            substrings.popleft()
            collected_colors.append(string)
        else:
            if len(substrings[0]) > 1:
                substrings.insert(len(substrings) // 2, substrings[0][:-1])
                substrings.popleft()
            else:
                substrings.popleft()
            if len(substrings[-1]) > 1:
                substrings.insert(len(substrings) // 2, substrings[-1][:-1])
                substrings.pop()
            else:
                substrings.pop()

    else:
        string = substrings[0]
        if string in main_colors + list(secondary_colors.keys()):
            substrings.pop()
            collected_colors.append(string)
        else:
            break

for color in collected_colors:
    if color in secondary_colors:
        for color_ in secondary_colors[color]:
            if color_ not in collected_colors:
                collected_colors.remove(color)

print(collected_colors)