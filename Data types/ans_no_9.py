#program to change a given string to new string where the first and 
# last chars have benn exchanged.

def exchange_first_last_char(str1):
    return str1[-1] + str1[1:-1] + str1[0]

#user input
user_input = input('Enter the string: ')

#function call
result = exchange_first_last_char(user_input)

#display the result
print(result)