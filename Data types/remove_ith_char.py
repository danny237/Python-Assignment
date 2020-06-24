#progran to remove i'th char from string

#function that remove i'th char
def remove_char(str1, i):
    result_str = ''
    for e in range(len(str1)):
        if e != i:
            result_str = result_str + str1[e]   
    return result_str

#User input
user_input = input('Enter the string: ')
index = int(input('Enter the index: '))

#function call
result = remove_char(user_input, index)

#display the result
print(result)