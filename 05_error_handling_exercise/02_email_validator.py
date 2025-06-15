class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_NAME_LENGTH = 5
CORRECT_DOMAINS = ["com", "bg", "org", "net"]

while True:
    command = input()
    if command == "End":
        break

    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")

    name, rest = command.split("@")
    if len(name) < MIN_NAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    if "." not in rest:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    domain = rest.split(".")[-1]
    if domain not in CORRECT_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")