# Write a Python program to sum all the items in a list.

def sum_list(num):
    sum =0
    for x in num:
        
            sum = sum + x
    return sum
print(sum_list([1,2,3]))