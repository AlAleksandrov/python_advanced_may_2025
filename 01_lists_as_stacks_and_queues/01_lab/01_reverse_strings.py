string = input().split()
reversed_string = []

while string:
    reversed_string.append(string.pop())


print(" ".join(reversed_string))