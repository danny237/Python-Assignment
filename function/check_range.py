


def check_range(n):
    if n in range(10, 20):
        print('it is in inside range.')
    else:
        print('it is not in inside range.')


x = int(input('Enter the number: '))
print(check_range(x))