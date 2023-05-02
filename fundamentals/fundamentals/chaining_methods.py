# Assignment: User
# For this assignment you will create the user class and add a couple methods!


class User:

    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Methods:
    # display_info(self) - Have this method print all 
    # of the users' details on separate lines.

    def display_info(self):
        print("==========================")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("==========================")

    def enroll(self):

        # NINJA BONUS
        # Add logic in the enroll method to check if 
        # they are a member already, and if they are, 
        # print "User already a member." and return False, otherwise return True.
        if(self.is_rewards_member):
            print("User already a member.")
            return self
        
        # Have this method change the user's member
        # status to True and 
        self.is_rewards_member = True

        # set their gold card points to 200.
        self.gold_card_points = 200

        return self

    
    
    def spend_points(self, amount):

        # Add logic in the spend points method
        # to be sure they have enough points to 
        # spend that amount and handle appropriately
        if self.gold_card_points < amount:
            print("Insufficient points.")
            return False

        # decrease the user's points by the amount specified.
        self.gold_card_points -= amount



my_user = User("Sadie", "Flick", "sflick@codingdojo.com", 39)
my_user.display_info()

user2 = User("Clifford", "Brown", "cbrown@codingdojo.com", 25)
user3 = User("Sonny", "Rollins", "srollins@codingdojo.com", 92)

my_user.spend_points(50)
user2.enroll().spend_points(80)

my_user.display_info()
user2.display_info()
user3.display_info()


# Terminal Output
## my_user information prints
## Insufficient points
## Prints my_user info again (doesn't change)
## User2 info -- 120 gold points, mem == True
## Show user 3 info, hasn't changed