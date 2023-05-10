class user:
    frist_name= CaleeAnn
    last_name= Wrath
    DOB= 04/12/1985
    email= caleeannwrath@gmail.com


class bank_account():
    def __init__(self, first_name, last_name, DOB, email, amount):
        self.first_name = first_name
        self.last_name = last_name
        self.checking_account = bank_account(300)
        self.savings_account = bank_account(300)
        self.balance = 0
        self.DOB = DOB
        self.email = email
        self.amount = amount

    def deposit(self):
        self.savings_account.deposit(500)
        print(self.savings_account.balance)
        return self

    def withdraw(self):
        self.checking_account.withdraw(100)
        print(self.checking_account.balance)
        return self
    
    def display_user_balance(self):
        self.checking_account.display_user_balance
        print('Your balance is' + (self.checking_account.display_user_balance))
        self.savings_account.display_user_balance
        print('Your balance is' + (self.savings_account.display_user_balance))
        return self
    
    def transfer_money(self):
        self.savings_account.transfer_money(100)
        self.checking_account.transfer_money(100)
        print((self.savings_account.balance) + 'has been transfered to'(self.checking_account.balance))


CaleeAnn_Checking = bank_account(300)
CaleeAnn_Savings = bank_account(300)