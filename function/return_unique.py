#program return unique value


def check_unique(list1):
    l = []
    for j in list1:
        if j not in l:
            l.append(j)
    return l
    

print('Enter the element for list (comma separator values): ')
list1 = [int(e) for e in input().strip().split(',')]

# function call
result = check_unique(list1)

print(result)
        