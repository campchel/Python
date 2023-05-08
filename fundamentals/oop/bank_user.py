class bank_account():
    default = []

    def __init__(self,int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        bank_account.default.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else: 
            print(f'Insufficient funds: Charging a $5 fee {self.balance - 5}')
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


    @classmethod
    def print_default(cls):
        for i in cls.default:
            print(.display_account_info)


CaleeAnn = bank_account(.01, 100)
Chelsey = bank_account(0.1, 200)


CaleeAnn.deposit(500).deposit(500).deposit(500).withdraw(300).yield_interest().display_account_info()
Chelsey.deposit(300).deposit(300).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()