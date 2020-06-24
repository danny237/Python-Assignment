#program to find largest number from list

def largest_number(list1):
    large_num = list1[0]
    for i in range(len(list1)-1):
        if large_num < list1[i+1]:
            large_num = list1[i+1]

    return large_num

# using max function
# def max_number(list1):
#     return max(list1)


# list
list1 = [11,2,3,4,10,0]

# function call
largest_num = largest_number(list1)
print(largest_num)