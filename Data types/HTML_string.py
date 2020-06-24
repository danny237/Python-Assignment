#Program that return html string with taga

#function to return string with tag
def add_tag(tag, word):
    opening_tag = '<' + tag + '>'
    closing_tag = '</' + tag + '>'
    return opening_tag + word + closing_tag

# User input
word = input('Enter the word: ')
tag = input('Enter the tag: ')

# function call
string_with_tag = add_tag(tag, word)

# Display the result
print(string_with_tag)
