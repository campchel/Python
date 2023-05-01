# 1
count=5
while count > 0:
    print(count)
    count = count - 1

# 2
def print_return(list):
    print(list[0])
    return list[1]

print(print_return([12,17]))

# 3
def one_length(list):
    return list[0] + len(list)

print(one_length([12,17]))

# 4
def greater_two(list):
    if len(list)< 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output

print(greater_two([12,13,17,18]))
print(greater_two([17]))

# 5
def length_value(value,size):
    output = []
    for i in range(0,size):
        output.append(value)
    return output
    
print(length_value(12,17))
print(length_value(13,18))


def value_length(value,size):
    output = []
    for i in range(1,value):
        output.append(size)
    return output

print(value_length(12,17))
print(value_length(13,18))
