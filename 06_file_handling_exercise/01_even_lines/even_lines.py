with open("text.txt") as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            clean_line = line.strip()
            for ch in "-,.!?":
                clean_line = clean_line.replace(ch, "@")
            reversed_words = " ".join(reversed(clean_line.split()))
            print(reversed_words)