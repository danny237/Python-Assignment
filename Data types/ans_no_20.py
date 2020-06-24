#fuction that print the string greater than 2 len and first and last same

def check(list1):
    # count = 0
    li = list(filter(lambda x: len(x) > 2, list1))
    equal = list(filter(lambda a: a[0] == a[-1], li))

    return len(equal)
    


sample_list = ['abc', 'xyz', '1441','f', 'ff']
l = check(sample_list)
print(l)
