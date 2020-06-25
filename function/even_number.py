# Program to print even number

def check_even(list1):
    l = []
    for x in list1:
        if x % 2 == 0:
            l.append(x)
    return l

# User input
print('Enter the element for list (comma seperated values): ')
list1 = [int(e) for e in input().strip().split(',')]
result = check_even(list1)

# display result
print(result)