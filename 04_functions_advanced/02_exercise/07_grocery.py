def grocery_store(**kwargs):
    sorted_result = sorted(kwargs.items(), key=lambda kvp: (-kvp[1],-len(kvp[0]), kvp[0]))
    string = ""
    for name, quantity in sorted_result:
        string += f"{name}: {quantity}\n"
    return string


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))