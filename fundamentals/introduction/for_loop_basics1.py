print("1 to 150")
n=0
while n <= 150:
    print(n, end='')
    n=n+1

print([i for i in range(5, 1000, 5 )])

def one_to_hundred():
    for i in range(1,100,1):
        if i % 5 == 0:
            print ('Coding')
        if i % 10 == 0:
            print ('Coding Dojo')

min = 0
max = 500000
Odds =0

for number in range(min, max, +1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Odds = Odds + number

print('Sum of Odds from {0} to {1} = {2}'.format(min, max, Odds))

def count_down_4():
    num= 2018
    while num > 0:
        print(num)
        num = num -4

count_down_4()

def flex_counter(lowNum, highNum, mult):
    for i in range(lowNum, highNum):
        if i % mult == 0:
            print(i)

flex_counter(3,6,9)