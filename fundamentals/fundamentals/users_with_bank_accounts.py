class bank_account():

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bank_account(int_rate=0.02, balance=0)
        self.balance = 0
    
    def deposit(self):
        self.account.deposit(100)
        print(self.account.balance)
        return self
    
    def withdraw(self, amount):
        self.account.withdraw(50)
        print(self.account.balance)
        return self
    
    def display_user_balance(self, amount):
        self.account.display_user_balance
        print('Your balance is' + (self.account.display_user_balance))
        return self
    
    def display_account_info(self):
        print(self.balance)
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            print('Balance:' + self.balance)
        else: 
            print('Your account balance is overdrawn')
        return self




CaleeAnn = bank_account(.01, 100)
Chelsey = bank_account(0.1, 200)

