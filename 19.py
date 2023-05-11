"""Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is"""


def newString(string):
    
    if "Is" in string:
        print("Is is present")
        
    else:
        return "Is " +  string
string = input("ENTER THE STRING ")
print(newString(string))
    