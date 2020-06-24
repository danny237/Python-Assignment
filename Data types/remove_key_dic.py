#program to remove a key from a dictionary

dic = {'country': 'Nepal', 'AKA': 'Gorkhali', 'mountain': 'Mt. Everest'}

print(dic)
key = input('Enter the key to remove: ')

del dic[key]

print(dic)