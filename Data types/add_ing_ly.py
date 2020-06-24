#function to add ing and ly if len of string > 3
def add_chars(str):
    if len(str) >= 3:
        if str[-3:] == 'ing':
            return str + 'ly'
        else:
            return str + 'ing'
    else:
        return str

#user input
user_input = input('Enter the string: ')

#function call and save to result
result = add_chars(user_input)

#display the result
print(result)