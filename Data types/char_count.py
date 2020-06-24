# function to count the string
def count_stirng(str):
    #create empty dictionary
    result_dict = dict()
    for i in str:
        if i != ' ':
            if i in result_dict:
                result_dict[i] += 1
            else:
                result_dict[i] = 1
                
    return result_dict

#function to display the string
def display_result(result):
    print(result)



# user input
user_input = input('Enter the string: ').strip()

# function call and save in counted_string
counted_string = count_stirng(user_input)

# display the result
display_result(counted_string)
