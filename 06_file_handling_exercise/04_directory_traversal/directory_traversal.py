import os


files = {}
folder = "../"

def get_files(directory, level):
    if level < 0:
        return

    for el in os.listdir(directory):
        if el == "report.txt":
            continue

        file = os.path.join(directory, el)

        if os.path.isfile(file):
            ext = os.path.splitext(el)[1]
            if ext not in files:
                files[ext] = []
            files[ext].append(el)

        else:
            get_files(file, level - 1)


get_files(folder, 1)

report_path = os.path.join(folder, "report.txt")

with open(report_path, "w") as f:
    for extensions, file_names in sorted(files.items()):
        f.write(f"{extensions}\n")
        for file_name in sorted(file_names):
            f.write(f"- - - {file_name}\n")