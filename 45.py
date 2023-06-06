# def prime(n):
#     if(n==1 or n==0):
#         return "INVALID INPUT"
#     flag =0
#     for i in range(2,n//2+1):
#         if(n%i==0):
#             flag =1;break
#     if(flag==0):
        
#         return "PRIME NUMBER"

#     else:
#         return "NOT PRIME NUMBER"
# n = int(input())
# print(prime(n))

# for i in range(2,n+1):
#     if (n%i==0):
#         print(i,end="")
    
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'PRIME_NO' function below.
#
# The function accepts INTEGER n as parameter.
#

def PRIME_NO(n):
    if(n==2):
        return True
    elif(n==1 or n==0):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

#
# Complete the 'PRIME_NOS_UPTO_N' function below.
#
# The function accepts INTEGER n as parameter.
#

def PRIME_NOS_UPTO_N(n):
    f = 1
    if(PRIME_NO(n)):
        print("PRIME NUMBER")
    else:
        print("NOT PRIME NUMBER")

    for i in range(2,n+1):
        if(PRIME_NO(i)):
            print(i, end=" ")
            f = 0
    if(f):
        print("INVALID INPUT")

# if _name_ == '_main_':
    n = int(input().strip())

    PRIME_NO(n)

    PRIME_NOS_UPTO_N(n)