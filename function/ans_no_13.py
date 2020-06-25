# Write a Python program to sort a list of tuples using Lambda.





# list of tuples
details = [('daniel', 22), ('sub', 26), ('kir', 11)]
print('Before: ', details)

# sort using sort and lambda
details.sort(key = lambda a: a[1])

# display the result
print('After:  ',details)

