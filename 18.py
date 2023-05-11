"""Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum."""

def sum(num1,num2,num3):
   
    sum  = num1+num2+num3
    if num1==num2==num3:
        sum = sum * 3
        return sum


print(sum(3,2,3))       
    
            