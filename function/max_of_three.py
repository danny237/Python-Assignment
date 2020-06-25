#program that print max of three numbers

# function return the max of three
def max_of_three(x, y, z):
    if x > y and x > z: return x
    elif y > x and y > z: return y
    else: return z


# user input
list1 = []
for i in range(3):
    m = int(input(str(i) + '.Enter the number: '))
    list1.append(m)
x, y, z = list1


result = max_of_three(x, y, z)
print(result)

