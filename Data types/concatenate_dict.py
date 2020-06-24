#Program that add key to dictionary

# function that add new key in dictionary
def add_key(dic1, dic2, dic3):
    dic = {}
    for d in (dic1, dic2, dic3):
        dic.update(d)
    return dic


# user input
print('1.Enter the key and values seperated by space: ')
dic1 = [e for e in input().strip().split()]

print('2.Enter the key and values seperated by space: ')
dic2 = [e for e in input().strip().split()]

print('3.Enter the key and values seperated by space: ')
dic3 = [e for e in input().strip().split()]


key1 = dict()
key1[dic1[0]] = dic1[1]

key2 = dict()
key2[dic2[0]] = dic2[1]

key3 = dict()
key3[dic3[0]] = dic3[1]

# function call
result = add_key(key1, key2, key3)

# display the result
print(result)