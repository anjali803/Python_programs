"""
Write a Python program that accepts a filename from the user and prints the extension of the file. 
Sample filename : abc.java
Output : java
"""
filename = input("ENTERT THE FILE NAME :")
f_extns = filename.split(".")
print("EXTENSION OF THE FILE :"+repr(f_extns[-1]))
