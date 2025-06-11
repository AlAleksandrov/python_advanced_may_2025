def list_roman_emperors(*args, **kwargs):
    successful_emperors ={}
    unsuccessful_emperors = {}
    for emperor_stat in sorted(args):
        name, status = emperor_stat[0], emperor_stat[1]
        if status:
            successful_emperors[name] = kwargs[name]
        else:
            unsuccessful_emperors[name] = kwargs[name]

    result = f"Total number of emperors: {len(args)}"
    if successful_emperors:
        result += f"\nSuccessful emperors:"
        successful_sorted = sorted(successful_emperors.items(), key=lambda kvp: (-kvp[1], kvp[0]))
        for key, value in successful_sorted:
            result += f"\n****{key}: {value}"
    if unsuccessful_emperors:
        result += f"\nUnsuccessful emperors:"
        unsuccessful_sorted = sorted(unsuccessful_emperors.items(), key=lambda kvp: (kvp[1], kvp[0]))
        for key, value in unsuccessful_sorted:
            result += f"\n****{key}: {value}"

    return result


print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))
