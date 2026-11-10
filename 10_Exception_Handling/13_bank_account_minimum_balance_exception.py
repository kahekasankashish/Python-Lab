# Q13. Create a Python program that implements a BankAccount class with methods for deposit and withdraw operations. The account must maintain a minimum balance of ₹1000. If the withdrawal amount violates the minimum balance rule, raise and handle a user-defined exception.
class MinimumBalanceError(Exception):
    pass


class BankAccount:
    MINIMUM_BALANCE = 1000

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print("New balance:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < self.MINIMUM_BALANCE:
            raise MinimumBalanceError(
                "The account must maintain a minimum balance of ₹1000. Withdrawal not possible."
            )
        self.balance -= amount
        print("New balance:", self.balance)


account = BankAccount(12000)
print("Old balance:", account.balance)
try:
    account.deposit(1000)
    account.withdraw(2000)
except (MinimumBalanceError, ValueError) as error:
    print(error)
