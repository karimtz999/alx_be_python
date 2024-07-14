class InsufficientFundsError(Exception):
    def __str__(self):
        return "Insufficient funds."

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            raise InsufficientFundsError()

    def display_balance(self):
        return f"Current Balance: ${self.account_balance}"

    def print_balance(self):
        print(f"Current balance: ${self.account_balance}")

