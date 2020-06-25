# Python program to find if a given string starts with a given character
# using Lambda.


str = input('Enter the string: ')
check = input("Enter the char to check starts with: ")

start_with = lambda x: True if str.startswith(check) else False
print(start_with(str))