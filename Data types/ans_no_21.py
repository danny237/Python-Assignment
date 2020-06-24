#Program that sorted the list increasing order by the last lement in tuple


list1 = [(2,1), (1,2), (2,3), (4,4), (2,5)]

result = sorted(list1, key = lambda a: a[1])
print(result)