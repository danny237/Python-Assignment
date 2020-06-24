#program to find largest number from list

def largest_number(list1):
    smallest_num = list1[0]
    for i in range(len(list1)-1):
        if smallest_num > list1[i+1]:
            smallest_num = list1[i+1]

    return smallest_num




# list
list1 = [1,2,3,4,10]

# function call
largest_num = largest_number(list1)
print(largest_num)