elements = set()

for _ in range(int(input())):
    for compounds in input().split():
        elements.add(compounds)


print(*elements, sep="\n")