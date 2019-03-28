# GeethaKarthikesan 2019
# program to output date and time
# datetime.py


# import datetime
import datetime

#rightnow =datetime.datetime.now()
rightnow = datetime.datetime.now()

#dayOfMonth = rightnow.day
dayOfMonth = rightnow.day


# dateAppendix based on dates
if dayOfMonth in [1, 21, 31]:
    dateAppendix = "st"    
elif dayOfMonth in [2, 22]:
    dateAppendix = "nd"
elif dayOfMonth in [3,23]:
     dateAppendix ="rd"   
else:
    dateAppendix = "th"


# using rightnow.strftime  for day, month,date,year,hour,minute,amorpm
day = rightnow.strftime("%A")
month = rightnow.strftime("%B")
date = rightnow.strftime("%d")
year = rightnow.strftime("%Y")
hour = rightnow.strftime("%I")
minute = rightnow.strftime("%M")
amOrpm = rightnow.strftime("%p")

#print the o/p in the asked format of day,month date year "at" hour am/pm
print (day + ", " + month + " " + date + dateAppendix + " " + year + " at " + hour + ":" + minute + amOrpm)
