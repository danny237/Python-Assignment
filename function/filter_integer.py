# Python program to square and cube every number in a given list of
# integers using Lambda.

list1 = [3,4,5,6,7]
print('Before:', list1)

# square
square_list = list(map(lambda a: a*a, list1))
print('Abter square: ', square_list)

# cube
cube_list = list(map(lambda a: a*a*a, list1))
print('After cube: ', cube_list)