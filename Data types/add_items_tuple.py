#program to convert tuple to a string
# add items in tuple

print('Enter the space seperated value.')
dic2 = tuple([int(e) for e in input().strip().split()])
print('Tuple: ', dic2)

list1 = list(dic2)
value = int(input('Enter the value to add: ').strip())
list1.append(value)
print(tuple(list1))