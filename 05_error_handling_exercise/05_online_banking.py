class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass

LEGAL_AGE = 18
pin, balance, age = input().split(", ")
balance = int(balance)
age = int(age)

while True:
    commands = input()
    if commands == "End":
        break

    command, *args = commands.split("#")
    if command == "Send Money":
        money, pin_code = float(args[0]), args[1]

        if money > balance:
            raise MoneyNotEnoughError('Insufficient funds for the requested transaction')

        if pin != pin_code:
            raise PINCodeError('Invalid PIN code')

        if age < LEGAL_AGE:
            raise UnderageTransactionError('You must be 18 years or older to perform online transactions')

        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif command == "Receive Money":
        money = float(args[0])
        if money < 0:
            raise MoneyIsNegativeError('The amount of money cannot be a negative number')
        else:
            print(f"{money / 2:.2f} money went straight into the bank account")
            balance += money / 2