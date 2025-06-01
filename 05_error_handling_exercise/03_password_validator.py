class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass

MIN_PASS_LONG = 8
SPECIAL_CHARS = ["@", "*", "&", "%"]

while True:
    command = input()
    if command == "Done":
        break

    if len(command) < MIN_PASS_LONG:
        raise PasswordTooShortError('Password must contain at least 8 characters')

    has_digit = any(char.isdigit() for char in command)
    has_letter = any(char.isalpha() for char in command)
    has_special = any(char in SPECIAL_CHARS for char in command)

    if not (has_digit or has_letter or has_special):
        raise PasswordTooCommonError('Password must be a combination of digits, letters, and special characters')

    if not has_special:
        raise PasswordNoSpecialCharactersError('Password must contain at least 1 special character')

    if " " in command:
        raise PasswordContainsSpacesError('Password must not contain empty spaces')

    print("Password is valid")