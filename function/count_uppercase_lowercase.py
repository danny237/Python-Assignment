#program to cuont lower and uppercase


upper_case = 0
lower_case = 0
def char_test(str1):
    global upper_case, lower_case
    for c in str1:
        if c.isupper():
            upper_case += 1
        elif c.islower():
            lower_case += 1
        else:
            pass


string1 = input('Enter the string: ')

char_test(string1)

print('No. of Upper case characters: ', upper_case)
print('No. of Lower case characters: ', lower_case)

