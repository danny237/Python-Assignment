# Write a Python program to check whether a given string is number or not
# using Lambda.


str = input('Enter something: ')

check_number = lambda a: True if a.isnumeric() else False
print(check_number(str))