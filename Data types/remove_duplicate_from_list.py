#function to remove duplicate from list

def remove_duplicate(list1):
    new_list = []
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    return new_list

#input for no of elements
n = int(input('No of elements: '))

list1 = []
for i in range(n):
    list1.append(int(input()))

# function call
result_list = remove_duplicate(list1)

#display the result
print(result_list)