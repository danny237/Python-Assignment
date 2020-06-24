#program that accept sentense and return sorted, unique word



#user input
#split the string by seperator ', '(comma + whitespace)
user_input = [e for e in input().strip().split(', ')]

#remove duplicate using set
#sorted the element using sorted method
sorted_words = sorted(set(user_input))

#display the result
print(', '.join(sorted_words))
