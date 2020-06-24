#fuction that counts the occurance of word
def word_count(str1):
    counts = dict()
    for i in str1:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

#user input
user_input = [e for e in input('Ehter the sentence: ').strip().split()]

#function call
word_count_result = word_count(user_input)

#display result
print(word_count_result)