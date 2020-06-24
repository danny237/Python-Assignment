# function to change string where all occurences of its 
# first char have been changed to $
def change_to(string):
    first_char = string[0]
    changed_char = string[1:].replace(first_char, '$')
    return first_char + changed_char

#function to display result
def display_result(result):
    print(result)


# user input
user_input = input('Enter the string: ').strip()

# function call and save in result
result = change_to(user_input)

# display the result
print(result)
