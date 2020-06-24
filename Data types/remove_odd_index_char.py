#program to remove the odd index values

#function to remove odd index
def remove_odd_index_char(str1):
    result_str = ''.join([str1[i] for i in range(len(str1)) if i % 2 != 0])
    return result_str


#user input
user_input = input('Enter the string: ')

#function call
result_str = remove_odd_index_char(user_input)

#display the result
print(result_str)


