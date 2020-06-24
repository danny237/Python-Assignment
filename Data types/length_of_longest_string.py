#def return the length of string
def length_of_string(str1):
    return len(str1)

#list of words
list_of_words = ['abc', 'wxyz', 'mn', 'p', 'jklmn']

# max length of the words
max_length = max(map(length_of_string, list_of_words))

#display the result
print(max_length)
