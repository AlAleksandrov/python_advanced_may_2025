def boarding_passengers(capacity, *args):
    program_dict = {}
    unsuccessful = False

    for guests, program in args:
        if capacity == 0:
            unsuccessful = True
            break

        if capacity >= guests:
            capacity -= guests

            if program not in program_dict:
                program_dict[program] = 0
            program_dict[program] += guests

        else:
            unsuccessful = True

    result = "Boarding details by benefit plan:"

    if program_dict:
        sorted_program = sorted(program_dict.items(), key=lambda kvp: (-kvp[1], kvp[0]))
        for benefit, passengers in sorted_program:
            result += f"\n## {benefit}: {passengers} guests"

    if capacity == 0 and not unsuccessful:
        result += "\nAll passengers are successfully boarded!"

    elif capacity == 0 and unsuccessful:
        result += "\nBoarding unsuccessful. Cruise ship at full capacity."

    elif capacity > 0:
        result += f"\nPartial boarding completed. Available capacity: {capacity}."

    return result


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
