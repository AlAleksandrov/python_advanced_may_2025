expression = input()
parentheses = {"{": "}", "[": "]", "(": ")"}
my_stack = []

for char in expression:
    if char in parentheses.keys():
        my_stack.append(char)
    elif char in parentheses.values():
        if not my_stack:
            print("NO")
            break
        last_parentheses = my_stack.pop()
        if parentheses[last_parentheses] != char:
            print("NO")
            break
else:
    if my_stack:
        print("NO")
    else:
        print("YES")