# Q5. Create a BankAccount class with accountNumber, accHolderName, accBalance and accType; implement withdraw(), deposit() and displayAccountDetails().
class BankAccount:
    def __init__(self, accountNumber, accHolderName, accBalance, accType):
        self.accountNumber = accountNumber
        self.accHolderName = accHolderName
        self.accBalance = float(accBalance)
        self.accType = accType

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.accBalance:
            print("Insufficient balance.")
        else:
            self.accBalance -= amount
            print(f"Balance after withdrawal: {self.accBalance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.accBalance += amount
            print(f"Balance after deposit: {self.accBalance:.2f}")

    def displayAccountDetails(self):
        print("Account number:", self.accountNumber)
        print("Account holder:", self.accHolderName)
        print(f"Account balance: {self.accBalance:.2f}")
        print("Account type:", self.accType)

account = BankAccount(1234, "Kashish", 20800, "Savings")
account.displayAccountDetails()
account.withdraw(1900)
account.deposit(5000)
account.displayAccountDetails()
