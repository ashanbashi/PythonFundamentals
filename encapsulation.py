#Hiding data so that other classes do not have access to it

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(2000)
account.deposit(600)
print(account.get_balance())

