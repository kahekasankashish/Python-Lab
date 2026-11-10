# Q4. Create an abstract PaymentGateway class with abstract methods pay(amount), refund(amount) and transaction_details(). Implement these methods in CreditCardPayment, DebitCardPayment and UPIPayment, and demonstrate each payment method using objects.
from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    @abstractmethod
    def transaction_details(self):
        pass


class CreditCardPayment(PaymentGateway):
    def __init__(self, amount):
        self.amount = amount

    def pay(self, amount):
        self.amount = amount
        print(f"Amount: {self.amount} paid via Credit Card.")

    def refund(self, amount):
        print(f"Amount: {amount} refunded via Credit Card.")

    def transaction_details(self):
        print("Credit Card Payment")


class DebitCardPayment(PaymentGateway):
    def __init__(self, amount=0):
        self.amount = amount

    def pay(self, amount):
        self.amount = amount
        print(f"Amount: {self.amount} paid via Debit Card.")

    def refund(self, amount):
        print(f"Amount: {amount} refunded via Debit Card.")

    def transaction_details(self):
        print("Debit Card Payment")


class UPIPayment(PaymentGateway):
    def __init__(self, amount=0):
        self.amount = amount

    def pay(self, amount):
        self.amount = amount
        print(f"Amount: {self.amount} paid via UPI.")

    def refund(self, amount):
        print(f"Amount: {amount} refunded via UPI.")

    def transaction_details(self):
        print("UPI Payment")


credit = CreditCardPayment(500)
debit = DebitCardPayment()
upi = UPIPayment()

for payment in (credit, debit, upi):
    payment.pay(500)
    payment.transaction_details()
    payment.refund(500)
    print()
