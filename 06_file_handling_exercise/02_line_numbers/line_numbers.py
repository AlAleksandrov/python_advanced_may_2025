from string import punctuation


with open("text.txt") as input_file, open("output.txt", "w") as output_file:

    for index, line in enumerate(input_file):
        all_letters = 0
        all_punctuations = 0
        clear_line = line.strip()

        for ch in clear_line:
            if ch.isalpha():
                all_letters += 1
            elif ch in punctuation:
                all_punctuations += 1

        output_file.write(f"Line {index + 1}: {clear_line} ({all_letters})({all_punctuations})\n")