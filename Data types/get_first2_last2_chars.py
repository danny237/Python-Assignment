# function that returns (first2 + last2) string
def get_first2_last2_chars(string):
    if len(string) < 2:
        return 'Empty String'
    else:
        return string[:2] + string[-2:]

# function to display result
def display_result(result):
    print(result)

# user input
user_input = input('Enter the string: ').strip()

# function call and save in result_stirng
result_string = get_first2_last2_chars(user_input)

# display result
display_result(result_string)


