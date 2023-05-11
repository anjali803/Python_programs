"""Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference"""

# num = int(input("ENTER A NUMBER :"))
# diff = num - 17
# print(diff)
# if num > 17:
#     print("greater")
    
# def diff(num):
#     if num > 17:
#         return num - 17
#     else :
#         return (num-17)*2
    
# # num = input("ENTER THE NUMBER :")
# print(diff(14))

def diff(num):
    if num <= 17:
        return num-17
    else :
        return (num-17)*2
num = int(input("enter then number"))
print(diff(num))