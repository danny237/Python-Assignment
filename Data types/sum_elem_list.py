#initializing the list
list1 = [1,2,5,3,5]

#function that return sum of all items in list
def sum(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum


print(sum(list1))