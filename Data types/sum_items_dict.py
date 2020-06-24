# Python program to sum all the items in a dictionary.
import functools

# Without using lambda function
# def sum_dic(dict1):
#     sum = 0
#     for i in dict1.values():
#         sum = sum + i

#     return sum



dic = {'one': 1, 'two': 2, 'three':3}

# without using lambda function
# result = sum_dic(dic)

# using lambda function
result = functools.reduce(lambda a,b: a + b, dic.values())

print(result)