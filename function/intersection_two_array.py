# Python program to find intersection of two given arrays using
# Lambda.


# first list
print('Enter the element of list (seperated by space)')
list1 = [int(e) for e in input().strip().split()]

# second list
print('Enter the element of list (seperated by space)')
list2 = [int(e) for e in input().strip().split()]

inter_list = list(filter(lambda a: a in list1,list2))

print(inter_list)
