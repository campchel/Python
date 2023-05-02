
class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member:
            print("user is enrolled as a member")
            return False
        self.is_rewards_member = True

    def points(self,amount):
        self.gold_card_points = 200

    def spend(self, amount):
        if self.gold_card_points < amount:
            return "Not enought points"
        
        self.gold_card_points = self.gold_card_points - amount


my_user = User("CaleeAnn", "Wrath", "caleeannwrath@gmail.com", 38)
my_user.display()
my_user.enroll()
my_user.display()
my_user.points(200)
my_user.display()
my_user.spend(20)
my_user.display()
