#program that return true if same key is already exist

#function to check
def check_exist(dic, key):
    if key in dic:
        return True
    else:
        return False

dic = {'name': 'Daniel', 'address': 'dhapakhel'}

# user input
key = input('Enter the key to check: ')

# function call
result = check_exist(dic, key)

# display the result
if result:
    print('Already exist.')
else:
    print('Not exists.')