def concatenate(*args, **kwargs):
    string = ""
    for word in args:
        string += word

    for key in kwargs:
        if key in string:
            string = string.replace(key, kwargs[key])

    return string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))