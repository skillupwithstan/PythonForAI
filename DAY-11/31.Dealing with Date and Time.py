import datetime

#print(dir(datetime))

# Get the current date and time
dtnow = datetime.datetime.now()
print(dtnow)

# Get current date
current_date = datetime.date.today()
print(current_date)

#print(datetime.date.weekday(datetime.date.today()))

# Date object to represent a date
dt = datetime.date(2023, 12, 25)
print(dt)

from datetime import date

# Get current date using today() method
todays_date = date.today()

print("Today's date =", todays_date)
print("Current year:", todays_date.year)
print("Current month:", todays_date.month)
print("Current day:", todays_date.day)

'''
from datetime import datetime

#dtnow = datetime.datetime.now()
#print(dtnow)

# current date and time
dtnow = datetime.now()
print("Current DateTime:",dtnow)

t = dtnow.strftime("%H:%M:%S")
print("Time:", t)

s1 = dtnow.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = dtnow.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

import datetime

print(datetime.datetime.now()+datetime.timedelta(minutes=15))
print(datetime.datetime.now()-datetime.timedelta(minutes=15))
