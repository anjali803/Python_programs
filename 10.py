"""Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615"""

n = int(input("ENTER THE SAMPLE VALUE :"))
a1= int("%s" %n)
a2= int("%s%s"%(n,n))
a3= int("%s%s%s"%(n,n,n))
print(a1+a2+a3)


# star = input("enter the symbol")
# a1 = ("%s\n"%star)
# a2 = ("%s%s\n"%(star,star))
# a3 = ("%s%s%s\n"%(star,star,star))
# print(a1+a2+a3)