# Program that insert a given string at the beginning of all items in list

# function to add string
def add_string(list1, str1):
    new_list = []
    for i in list1:
        new_ele = str1 + str(i)
        new_list.append(new_ele)

    return new_list

#user input
print('Enter the element seperated by space.')
list1 = [e for e in input().strip().split()]
str1 = input('Enter the string: ')

# function call
result_list = add_string(list1, str1)



# new_list = add_string()
print(result_list)
