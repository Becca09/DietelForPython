class Account:

    def __init__(self, name, acct_number):
        self.name = name
        self.balance = 0
        self.acct_number = acct_number

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if self.balance - amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance = self.balance - amount

    def transfer(self, amount, account):
        if self.balance < amount:
            raise ValueError("Balance cannot be less than amount")

        self.balance = self.balance - amount
        account.balance = account.balance + amount

    def load_airtime(self, amount):
        if self.balance - amount < 0:
            raise ValueError("balance cannot be less than amount")
        self.balance = self.balance - amount
