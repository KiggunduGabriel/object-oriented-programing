class BankAccount:
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance+= amount

    def withdraw(slef, amount):
        slef.balance -= amount

account= BankAccount(230)
account.deposit(70)
account.withdraw(160)
print(f"the account balance is",account.balance)                