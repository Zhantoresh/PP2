"""
Create a bank account class that has attributes owner, 
balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, 
and test to make sure the account can't be overdrawn.

class Account:
    pass
"""
class Bank:
    def __init__(self, money):
        self.balanc = money

    def balance(self):
        print(f'balance: {self.balanc}')

    def deposit(self, dep):
        self.balanc += dep
        print(f'deposit of {dep} successfully made. New balance: {self.balanc}')

    def withdraw(self, wit):
        if self.balanc < wit:
            print('insufficient funds!')
        
        else:
            self.balanc -= wit
            print(f'withdrawal of {wit} successfully made. New balance: {self.balanc}')


user = Bank(1000)

user.balance()
user.deposit(100)
user.balance()
user.withdraw(1200)
user.withdraw(1000)