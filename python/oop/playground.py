class BankAccount:

    def __init__(self, owner):
        self.balance = 0
        self.owner = owner
        print(f"opened account for new owner {owner}")

    def deposit(self, amount):
        self.balance += amount
        print(f". Deposit. new balance for {self.owner} is {self.balance}")
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        print(f". Withdraw. new balance for {self.owner} is {self.balance}")
        return self.balance


acct = BankAccount("Darcy")
acct.deposit(10)
acct.withdraw(3)
