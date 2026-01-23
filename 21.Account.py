class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount): 
        self.balance += amount
        print(f"Deposited: ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew: ${amount}. Remaining: ${self.balance}")
        else:
            print("Not enough balance!")

bal=float(input("Enter balance: "))
acc=Account(bal)
dep=float(input("Enter deposit: "))
acc.deposit(dep)
wd=float(input("Enter amount to withdraw: "))
acc.withdraw(wd)
