"""
Create a bank account class that has attributes owner, 
balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, 
and test to make sure the account can't be overdrawn.

class Account:
    pass
"""
class jeke():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    
    def teks(self):
        print(f"Balance is {self.balance}")

    def deposit(self, ai):
        self.balance += ai
        print(f"{ai} has been deposited")

    def withdraw(self, ai):
        if ai > self.balance:
            print("Not enough cash on balance")
        else:
            self.balance -= ai
            print(f"{ai} has been withdrawn from deposit")

own1 = jeke("Birzhan")

own1.teks()
own1.deposit(5000)
own1.teks()
own1.withdraw(2000)
own1.teks()