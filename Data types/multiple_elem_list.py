#program to multiple all element of list
 
import functools
list1 = [1,2,3,4]
result = functools.reduce(lambda a,b: a * b, list1)

print(result)