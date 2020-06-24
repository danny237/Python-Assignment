#program to check the list is empty or not

def check_empty(a):
    if a:
        return 'List is not empty.'
    else:
        return 'List is empty.'

#user input 
user_input = input('Enter the element in list: ')

list1 = list(user_input)
print(list1)