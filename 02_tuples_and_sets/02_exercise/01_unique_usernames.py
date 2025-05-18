names_set = set()

for _ in range(int(input())):
    usernames = input()
    names_set.add(usernames)

print(*names_set, sep="\n")