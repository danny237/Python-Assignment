#fuction that
def insert_string_middle(string, middle):
    l = len(string)
    mid = l // 2
    right = string[mid:] 
    left = string[0:mid]
    return left + middle + right




#user input
input_string = input('Enter the string: ')
middle_string = input('Enter the string to insert in middle: ')

#function call
result_string = insert_string_middle(input_string, middle_string)

#display result
print(result_string)