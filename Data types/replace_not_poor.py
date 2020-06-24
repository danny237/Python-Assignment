#function that replace 'not'...'poor' to 'good'
def replace_not_poor(str1):
    index_of_not = str1.find('not')
    index_of_poor = str1.find('poor')

    #if 'not' follows the 'poor'
    if index_of_not < index_of_poor:
        return str1[:index_of_not] + 'good' + str1[index_of_poor + 4:]
    else:
        return "'not' not follows 'poor'"

#user input
user_input = input('Enter the string: ')

# function call and save returned value to result
result = replace_not_poor(user_input)

#display the value
print(result)