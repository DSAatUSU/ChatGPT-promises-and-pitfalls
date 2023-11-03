class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        """Method to deposit money into the bank account"""
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid amount for deposit")

    def withdraw(self, amount):
        """Method to withdraw money from the bank account"""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient balance")
        else:
            print("Invalid amount for withdrawal")


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        super().__init__()
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        """Method to withdraw money from the minimum balance account"""
        if self.balance - amount >= self.minimum_balance:
            super().withdraw(amount)
        else:
            print("Minimum balance limit reached")


class MaximumBalanceAccount(BankAccount):
    def __init__(self, maximum_balance):
        super().__init__()
        self.maximum_balance = maximum_balance

    def deposit(self, amount):
        """Method to deposit money into the maximum balance account"""
        if self.balance + amount <= self.maximum_balance:
            super().deposit(amount)
        else:
            print("Maximum balance limit reached")
