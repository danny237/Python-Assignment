#function that copy the list 

#input for no of elements
n = int(input('Enter the no. of elements in list: '))

list1 = []
for i in range(n):
    list1.append(int(input()))

list2 = list1.copy()

# Display the result
print(list1)
print('id of list1: ',id(list1))
print(list2)
print('id of list2: ',id(list2))
