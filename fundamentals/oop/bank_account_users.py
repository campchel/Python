class user():
    def __init__(self, first_name, last_name, DOB, email, ):
        self.first_name = first_name
        self.last_name = last_name
        self.DOB = DOB
        self.email = email

class bank_account():
    def __init__(self, account, amount, balance):
        self.account = account
        self.balance = balance

    def deposit(self):
        self.deposit(500)
        print(self.balance)
        return self

    def withdraw(self):
        self.withdraw(100)
        print(self.balance)
        return self
    
    def display_user_balance(self):
        self.display_user_balance
        print('Your balance is' + (self.display_user_balance))
