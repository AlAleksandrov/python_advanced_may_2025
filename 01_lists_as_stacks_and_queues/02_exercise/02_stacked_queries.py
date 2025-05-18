number = int(input())
stack = []

for i in range(number):
    queries = input().split()
    if queries[0] == "1":
        stack.append(int(queries[1]))
    elif stack:
        if queries[0] == "2":
            stack.pop()
        elif queries[0] == "3":
            print(max(stack))
        elif queries[0] == "4":
            print(min(stack))


print(", ".join([str(x) for x in reversed(stack)]))
