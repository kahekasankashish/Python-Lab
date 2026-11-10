# Q12. Write a Python program to simulate ATM withdrawal. If the withdrawal amount is greater than the account balance or exceeds ₹20000 per day, raise a user-defined exception.
class WithdrawalError(Exception):
    pass

account_balance = float(input("Enter the account balance: "))
daily_withdrawn = float(input("Enter amount already withdrawn today: "))
withdrawal_amount = float(input("Enter amount to be withdrawn: "))

try:
    if withdrawal_amount <= 0:
        raise WithdrawalError("Withdrawal amount must be positive.")
    if withdrawal_amount > account_balance:
        raise WithdrawalError("Insufficient account balance.")
    if daily_withdrawn + withdrawal_amount > 20000:
        raise WithdrawalError("Daily withdrawal limit of ₹20000 exceeded.")
    account_balance -= withdrawal_amount
    daily_withdrawn += withdrawal_amount
    print("Withdrawal successful.")
    print("Remaining account balance:", account_balance)
    print("Total withdrawn today:", daily_withdrawn)
except WithdrawalError as error:
    print(error)
