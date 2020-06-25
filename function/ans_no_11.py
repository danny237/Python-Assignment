# Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.


def add(n):
    x = lambda a: a +15
    return x(n)
x = int(input('enter the number to add 15 on it: '))
print(add(x))



def mul(x, y):
    ans = lambda x, y: x*y
    return ans(x,y)
print('For multiplication: ')
a = int(input('enter the value of a: '))
b = int(input('enter the value of b: '))
print(mul(3,4))