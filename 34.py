# Armstrong number
n = int(input())
cnt = 0
sum = 0
n_cpy =n
while(n>0):
    cnt = cnt+1
    n=n//10
n=n_cpy
while(n>0):
    ld = n%10
    sum = sum + ld**cnt
    n = n//10
n = n_cpy
if(sum ==n):
    print("yes")
else:
    print("no")

# input:1634
