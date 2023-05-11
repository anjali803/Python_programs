# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
#  Expected Result : 2

def mystring(words):
    ctr = 0
    for x in words:
        if (x[0]==x[-1]):
            ctr+=1
            
    return ctr
print(mystring(['abc', 'xyz', 'abcda', '1221']))