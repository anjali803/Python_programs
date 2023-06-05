#print all the divisors of n among them print even numbers only
n = int(input())
for i in range(1,n//2+1):
    if(n%i==0 and i%2==0):
        print(i,end=" ")
    