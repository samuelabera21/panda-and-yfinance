class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


def run_demo():
    print("ENCAPSULATION DEMO")
    account = BankAccount("Riya", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Owner: {account.owner}")
    print(f"Balance (using getter): {account.get_balance()}")
    print()
