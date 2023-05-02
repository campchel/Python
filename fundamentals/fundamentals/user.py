
class User:

    def __init__(self, first_name, last_name, email, age, gender, marital_status):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.gender = gender
        self.marital_status = marital_status

    def display(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Points: {self.gold_card_points}")
        print(f"Gender: {self.gender}")
        print(f"Marital Status: {self.marital_status}")

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


user1 = User("CaleeAnn", "Wrath", "caleeannwrath@gmail.com", 38, "Female", "Married")
user1.display()
user1.enroll()
user1.display()
user1.points(200)
user1.display()
user1.spend(50)
user1.display()

user2 = User("Chelsey", "Campbell", "cc.chels.campbell@gmail.com", 38, "Female", "Single")
user1.display()
user1.enroll()
user1.display()
user1.points(200)
user1.display()
user1.spend(80)
user1.display()
