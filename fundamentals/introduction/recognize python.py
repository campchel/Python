# variable declarations
    # data types- primitive- numbers
num1 = 42 
    # data types- primitive- numbers with decimals
num2 = 2.3
    # data types- primitive- boolean
boolean = True
    # data types- primitive- strings
string = 'Hello World'
    # data types- composite- list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
    # data types- composite- tuples
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
    # data types-composite- list
fruit = ('blueberry', 'strawberry', 'banana')
    # log statement
print(type(fruit))
print(pizza_toppings[1])
    # add value
pizza_toppings.append('Mushrooms')
    # log statement
print(person['name'])

person['name'] = 'George'
person['eye_color'] = 'blue'
    # log statement
print(fruit[2])
    # conditional- if number is greater than 45 log statement
if num1 > 45:
    print("It's greater")
    # conditional- if its not greater than 45 log statement
else:
    print("It's lower")

    # conditional- if the length of the string is less than 5 log statement
if len(string) < 5:
    print("It's a short word!")
    # conditional- if the length of the string is greater than 15 log statement
elif len(string) > 15:
    print("It's a long word!")
    # conditional- if the lngth of the string isn't less than 5 nor greater than 15 log statement
else:
    print("Just right!")

    # for loop 1-4 and log statement
for x in range(5):
    print(x)
    # for loop 2-4 and log statement
for x in range(2,5):
    print(x)
    # for loop 2-9 with the increment of three and log statement
for x in range(2,10,3):
    print(x)
    # for loop with while statement- print as long as x is less than 5
x = 0
while(x < 5):
    print(x)
    x += 1

    # pop is removing the index from the list
pizza_toppings.pop()
pizza_toppings.pop(1)

    # log person statement, remove eye color and log new person statement
print(person)
person.pop('eye_color')
print(person)

    # for loop with if statements- if the topping is pepperoni than log statement, if topping is olive than break from for loop
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

    # define the function
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

    # single line comment
"""
Bonus section
"""

    # multiline comment
# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)