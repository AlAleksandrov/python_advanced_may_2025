text = input()

char_set = set(x for x in text)

for char in sorted(char_set):
    print(f"{char}: {text.count(char)} time/s")

