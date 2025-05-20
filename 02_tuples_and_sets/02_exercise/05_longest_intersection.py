def range_preparation(range_str):
    start, end = [int(x) for x in range_str.split(",")]
    lst = set(range(start, end + 1))
    return lst


def range_intersection(current_range):
    range_one, range_two = current_range.split("-")
    first_range = range_preparation(range_one)
    second_range = range_preparation(range_two)
    return first_range.intersection(second_range)


longest_intersection = set()

for _ in range(int(input())):
    curr_range = input()
    intersection = range_intersection(curr_range)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection


print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")