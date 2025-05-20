even_set = set()
odd_set = set()
counter = 0

for _ in range(int(input())):
    names = input()
    counter += 1
    summarize = 0
    for char in names:
        summarize += ord(char)
    result = summarize // counter
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)


if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(odd_set) < sum(even_set):
    print(*odd_set.symmetric_difference(even_set), sep=", ")