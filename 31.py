# DATE AND TIME IN PYTHON

# simple way to print date
import datetime
d=datetime.date(2023,4,13)
print(d)

# simple way to print today's date
import datetime
d= datetime.date.today()
print("current date =" ,d)


# printing current year,month and day
from  datetime import date
today = date.today()
print("current year :",today.year)
print("current month :",today.month)
print("current day :",today.day)


# printing time
from datetime import time
t = time()
print("time:",t) 

# Another way of printing time
from datetime import time 
Time = time(11,23,43)
print("Time",Time)

# current date and time
from datetime import datetime
dt = datetime.today()
print(dt)


# printing t1-t2
from datetime import timedelta
t1 = timedelta(weeks=1,days= 2,hours=1,seconds=30)
t2 = timedelta(days=3,hours=4,seconds=45)
print(t1-t2)

# printing date and time
from datetime import datetime
dt = datetime.now()
print("current date and time :" ,dt)

# using strftime method
dt.strftime("%H : %M : %S")
print("current date and time :" ,dt)

# dt.strftime("%d%m%Y,%H:%M:%S")

