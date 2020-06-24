#Program that add key to dictionary

# function that add new key in dictionary
def add_key(dict1, key):
    dict1.update(key)
    return dict1


dict1 = {'name': 'Daniel', 'address': 'Lalitpur'}
# user input
print('existing dict: ')
print(dict1)
print('Enter the key and values seperated by space: ')
user_input = [e for e in input().strip().split()]


key = dict()
key[user_input[0]] = user_input[1]

# function call
result = add_key(dict1, key)

# display the result
print(result)