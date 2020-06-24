# Program to replace the last element in a list with another list

# functio to replace last element
def replace_ele(list1, list2):
    list1[-1:] = list2
    return list1

# User input
print('Enter the elem of list seperated by space')
print('first list')
list1 = [int(e) for e in input().strip().split()]
print('second list')
list2 = [int(e) for e in input().strip().split()]

# Function call
result = replace_ele(list1, list2)

#display the result
print(result)