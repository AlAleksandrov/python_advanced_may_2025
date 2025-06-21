from collections import deque


mechanical_parts = [int(x) for x in input().split()]
power_cells = deque([int(x) for x in input().split()])
assembled_drones = []
drones = 0

SENTINEL = 100
VIPER = 85
AEGIS = 75
STRIKER = 65
TITAN = 55

while mechanical_parts and power_cells and len(assembled_drones) < 5:
    cell = power_cells.popleft()
    if cell == 0:
        continue

    part = mechanical_parts.pop()
    activation_power = part + cell

    if activation_power >= SENTINEL and "Sentinel-X" not in assembled_drones:
        assembled_drones.append("Sentinel-X")
        drones += 1

        if activation_power > SENTINEL:
            if cell - 30 > 0:
                power_cells.append(cell - 30)

        continue

    elif activation_power >= VIPER and "Viper-MKII" not in assembled_drones:
        assembled_drones.append("Viper-MKII")
        drones += 1

        if activation_power > VIPER:
            if cell - 30 > 0:
                power_cells.append(cell - 30)

        continue

    elif activation_power >= AEGIS and "Aegis-7" not in assembled_drones:
        assembled_drones.append("Aegis-7")
        drones += 1

        if activation_power > AEGIS:
            if cell - 30 > 0:
                power_cells.append(cell - 30)

        continue

    elif activation_power >= STRIKER and "Striker-R" not in assembled_drones:
        assembled_drones.append("Striker-R")
        drones += 1

        if activation_power > STRIKER:
            if cell - 30 > 0:
                power_cells.append(cell - 30)

        continue

    elif activation_power >= TITAN and "Titan-Core" not in assembled_drones:
        assembled_drones.append("Titan-Core")
        drones += 1

        if activation_power > TITAN:
            if cell - 30 > 0:
                power_cells.append(cell - 30)

        continue

    if cell - 1 > 0:
        power_cells.append(cell - 1)


if len(assembled_drones) == 5:
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")

if assembled_drones:
    print(f"Assembled Drones: {', '.join(str(x) for x in assembled_drones)}")

if mechanical_parts:
    print(f"Mechanical Parts: {', '.join(str(x) for x in mechanical_parts[::-1])}")

if power_cells:
    print(f"Power Cells: {', '.join(str(x) for x in power_cells)}")