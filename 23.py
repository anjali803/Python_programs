# Write a Python program to get the smallest number from a list

def smallest_num(list):
    smallest = list[0]
    for x in list:
        if x<smallest:
            smallest = x 
            
    return smallest 
print(smallest_num([2,3,6,4]))