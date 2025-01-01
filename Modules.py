#Random Modules:
import random
print(random.randint(0,5))
print(random.random())
print(random.random()*100)
list1=[2,4,5,790,'vignesh','sathish']
result=random.choice(list1)
print(result)

#Date and time modules:
import datetime
from datetime import date
import time

import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime('%a')) #a-short form of day
print(x.strftime('%A')) #A-Day
print(x.strftime('%B')) #B-Month
print(x.strftime('%b')) #b-short form of month

import datetime
x=datetime.datetime(2024,10,17)
x1=datetime.datetime.now()
print(x)
print(x1)
import datetime
x=datetime.datetime(2024,5,31)
print(x.strftime('%B'))

#Calender Modules:
import calendar
print(calendar.month(2024,2))
#calendar of the year 2024
print(calendar.calendar(2025))
print(calendar.isleap(2024))
print(calendar.isleap(2025))
print(calendar.isleap(2023))


import calendar
print("the 4th month of 1997 is:")
calendar.prmonth(1997,1,3,2) #sets width between dates.
#using setfirstweekday()to set first weekday number
calendar.setfirstweekday(2)
print("first weekday after modification",calendar.firstweekday())
print(calendar.month(1997,4))
print(calendar.prcal(2026)) #print the given

import calendar
val=calendar.setfirstweekday(calendar.SATURDAY)
print(val)

import calendar
val=calendar.setfirstweekday(calendar.MONDAY)
print(val)
