number = int(input())
stack = []

for i in range(number):
    queries = input().split()
    if len(queries) > 1:
        stack.append(int(queries[1]))
    elif len(queries) == 1:
        if queries[0] == "2":
            if len(stack) > 0:
                stack.pop()
        elif queries[0] == "3":
            print(max(stack))
        elif queries[0] == "4":
            print(min(stack))


for _ in range(len(stack)):
    if len(stack) > 1:
        print(stack.pop(), end=", ")
    else:
        print(stack.pop())
