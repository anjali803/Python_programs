# # # print prime number
# # n = int(input())
# # flag = 0
# # for i in range(2,n//2+1):
# #     if(n%i==0):
# #         flag=1
# #         break
# # if(flag==0):
# #     print("prime")
# # else:
# #     print("not prime")
    
    
# # another way
# # n = int(input())
# # for i in range(2,n//2+1):
# #     if(n%i==0):
# #         print("not prime");break
# # else:
# #     print(" prime")



# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'PRIME_NO' function below.
# #
# # The function accepts INTEGER n as parameter.
# #

# def PRIME_NO(n):
#     # ---------------------------------------------------------

#     # WRITE YOUR CODE HERE...
#     if n<=1:
#         return "NOT PRIME NUMBER"
#     flag = 0
#     for i in range(2,n//2+1):
#         if(n%i==0):
#             flag=1
#             break
#     if(flag==0):
#         return "PRIME NUMBER"
#     else:
#         return "NOT PRIME NUMBER"

#     # ---------------------------------------------------------

# #
# # Complete the 'PRIME_NOS_UPTO_N' function below.
# #
# # The function accepts INTEGER n as parameter.
# #

# def PRIME_NOS_UPTO_N(n):
#     # ---------------------------------------------------------

#     # WRITE YOUR CODE HERE...
#     for i in range(2,n+1):
#         if(n%i==0):
#             return PRIME_NO(n)
#         else:
#             return "INVALID INPUT"
#     # ---------------------------------------------------------

#     if __name__ == '__main__':
#         n = int(input().strip())

#         PRIME_NO(n)

#         PRIME_NOS_UPTO_N(n)

    
def isprime(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return "NOT PRIME "
        return "PRIME NUMBER"
    else:
        return "INVALID INPUT"
print(isprime(64))
print(isprime(5))

