# Write a Python program to get the largest number from a list

def largest_num(list):
    largest = list[0]
    for x in list:
        if x > largest:
            largest = x
            
    return largest
print(largest_num([2,5,7,8,10]))