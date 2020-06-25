# program to check the prime or not

# func to check prime
def chceck_prime(list1):
    l = []
    for n in list1:
        if n == 1:
            pass
        elif n == 2:
            pass
        else:
            for x in (2, n):
                if n % x == 0:
                    pass
                else:
                    l.append(n)
    return l


# User input
print('Enter the element for list (seperated by comma): ')
list1 = [int(e) for e in input().strip().split(',')]

# function call
result = chceck_prime(list1)

# display the result
print(result)
