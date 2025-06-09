def plant_garden(space:float, *args, **kwargs):
    result = ''
    plant_result = ""
    counter = 0
    counter_plant = 0
    for plant in sorted(args):
        unique_plant_type, space_required_per_plant = plant[0], plant[1]
        if unique_plant_type in sorted(kwargs):
            counter_plant += 1

            if space == 0.0:
                continue

            elif space >= space_required_per_plant * kwargs[unique_plant_type]:
                space -= space_required_per_plant * kwargs[unique_plant_type]
                counter += 1
                plant_result += f"\n{unique_plant_type}: {kwargs[unique_plant_type]}"

            elif space % space_required_per_plant == 0:
                remainder = int(space / space_required_per_plant)
                space -= space_required_per_plant * remainder
                plant_result += f"\n{unique_plant_type}: {remainder}"

            elif space // space_required_per_plant > 0:
                remainder = int(space / space_required_per_plant)
                space -= space_required_per_plant * remainder
                plant_result += f"\n{unique_plant_type}: {remainder}"


    if counter == counter_plant:
        result = f"All plants were planted! Available garden space: {space:.1f} sq meters.\nPlanted plants:{plant_result}"
    else:
        result = f"Not enough space to plant all requested plants!\nPlanted plants:{plant_result}"

    return result


# print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
# print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
# print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))