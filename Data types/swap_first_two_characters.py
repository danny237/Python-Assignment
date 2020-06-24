#function that return first two string
def swap_first_two_string(str1, str2):
    first_str_after_swap = str2[:2] + str1[2:]
    second_str_after_swap = str1[:2] + str2[2:]
    return first_str_after_swap + ' ' + second_str_after_swap

# User input
first_str = input('Enter the first string: ')
second_str = input('Enter the second string: ')

#function call
result = swap_first_two_string(first_str, second_str)

#display the result
print(result)

