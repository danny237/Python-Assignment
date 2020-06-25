#program that print the sum of elements of list

# function that return sum of list
def sum_of_list(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum


print('Enter the element for list (comma separator values): ')
list1 = [int(e) for e in input().strip().split(',')]

result = sum_of_list(list1)
print(result)