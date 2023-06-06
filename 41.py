# 01.To check a number is prime or not
n = int(input())
flag = 0
for i in range(2,n//2+1):
    if(n%i==0):
        flag=1
        break
if(flag==0):
    print("prime")
else:
    print("Not prime")
    
# input:17