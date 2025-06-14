def accommodate(*args, **kwargs):
    unaccommodated_guests = 0
    accommodated_rooms = {}
    lst_idx = []
    room_dict = {}
    for x, y in kwargs.items():
        room_dict[int(x.split("_")[1])] = y

    for group in args:
        lst_idx.append(group)
        sorted_rooms = sorted(room_dict.items(), key=lambda kvp: (kvp[1], kvp[0]))
        for room, guest in sorted_rooms:

            if room_dict[room] == group:
                accommodated_rooms[room] = group
                del room_dict[room]
                lst_idx.remove(group)
                break

            elif room_dict[room] > group:
                accommodated_rooms[room] = group
                del room_dict[room]
                lst_idx.remove(group)
                break

    if lst_idx:
        unaccommodated_guests = sum(lst_idx)


    if not room_dict and not lst_idx:
        result = f"A total of {len(accommodated_rooms)} accommodations were completed!"

        for room_number, guests in sorted(accommodated_rooms.items()):
            result += f"\n<Room {room_number} accommodates {guests} guests>"

    elif not accommodated_rooms:
        result = f"No accommodations were completed!"

    else:
        result = f"A total of {len(accommodated_rooms)} accommodations were completed!"

        for room_number, guests in sorted(accommodated_rooms.items()):
            result += f"\n<Room {room_number} accommodates {guests} guests>"

    if unaccommodated_guests != 0:
        result += f"\nGuests with no accommodation: {unaccommodated_guests}"

    if len(room_dict) != 0:
        result += f"\nEmpty rooms: {len(room_dict)}"

    return result


print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(2, 2, 2, room_501=2, room_502=2))
print(accommodate(3, room_101=4, room_102=3))
print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
print(accommodate(2, 4, 3, room_101=2, room_102=3, room_103=4))
print(accommodate(7, 4, room_201=4, room_202=5))
print(accommodate(6, 5, 4, room_301=1, room_302=2, room_303=3))
print(accommodate(2, 3, room_401=4, room_402=4))
