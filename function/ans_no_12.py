# Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

def func_compute(n):
    return lambda x : x * n
result = func_compute(2)
print("Multiplicatio of 2 adn 15 is : ", result(15))