from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")


class CreditCard(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


p1 = UPI()
p1.pay(500)

p2 = CreditCard()
p2.pay(1200)