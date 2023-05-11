# Write a Python program to multiply all the items in a list.

def mul_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(mul_list([1,2,3]))