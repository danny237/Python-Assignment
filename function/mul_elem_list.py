#program that print the multiple of elements of list

# function that return sum of list
def mul_of_list(list1):
    mul = 1
    for i in list1:
        mul *= i
    return mul


print('Enter the element for list (comma separator values): ')
list1 = [int(e) for e in input().strip().split(',')]

result = mul_of_list(list1)
print(result)