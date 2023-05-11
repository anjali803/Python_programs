"""Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module."""

import calendar 
yy = int(input("ENTER THE YEAR :"))
mm = int(input("ENTER THE MONTH :"))
print(calendar.month(yy,mm))