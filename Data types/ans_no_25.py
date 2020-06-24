#program that print true if the dict in list is empty

#function to check empty or not
def check_empty(li):
    for i in li:
        if i:
            return False
        else:
            return True

# sample empty list
sample_empty_list = [{}, {}, {}]
sample_non_empty_list = [{1,2}, {}, {}]

# function call
# for empty 
result = check_empty(sample_empty_list)
print(result)

# for non-empty
result1 = check_empty(sample_non_empty_list)
print(result1)

