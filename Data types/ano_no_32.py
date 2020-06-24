# python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x)

# function that generate number
def generate(n):
    dic = dict()
    for i in range(1,n+1):
        dic[i] = i*i
    return dic

# user input
user_input = int(input('Enter the number: '))

# function call
result = generate(user_input)

# display the result
print(result)

