expression = list(input())
stack = []

for index, string in enumerate(expression):
    if string == "(":
        stack.append(index)
    elif string == ")":
        print("".join(expression[stack.pop():index + 1]))