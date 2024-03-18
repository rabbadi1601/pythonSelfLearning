import datetime

Time_of_Booking = datetime.datetime.now()
print(Time_of_Booking)
date = Time_of_Booking.date()
print(date)
date = date.strftime("%d-%m-%y")
print(date)

print(Time_of_Booking.time().strftime("%H:%M:%S %p"))

'''
output:
2024-03-14 17:40:58.268534
2024-03-14
14-03-24
17:40:58 PM

https://www.w3schools.com/python/python_datetime.asp
'''