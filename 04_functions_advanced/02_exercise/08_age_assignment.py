def age_assignment(*args, **kwargs):
    result = ""
    for key, age in sorted(kwargs.items(), key=lambda kvp: kvp[0]):
        for name in args:
            if key in name:
                result += f"{name} is {age} years old.\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))