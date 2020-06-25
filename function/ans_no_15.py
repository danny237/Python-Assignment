# Write a Python program to filter a list of integers using Lambda.


list1 = [3,4,5,6,7,10]

new_list = list(filter(lambda a:a % 2 == 0, list1))
print(new_list)