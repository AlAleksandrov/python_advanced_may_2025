def even_odd_filter(**kwargs):
    current_result = {}
    for key in kwargs:
        if key == "odd":
            result = [int(x) for x in kwargs["odd"] if x % 2 != 0]
            kwargs["odd"] = result
        if key == "even":
            result = [int(x) for x in kwargs["even"] if x % 2 == 0]
            kwargs["even"] = result

    current_result = dict(sorted(kwargs.items()))

    return current_result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
