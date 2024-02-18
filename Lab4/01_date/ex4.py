'''
Write a Python program to calculate two date difference in seconds.
'''
import datetime

date1 = datetime.date(2024,2,25)
date2 = datetime.date(2024,2,20)
difference = date1 - date2 
seconds = difference.total_seconds()
print(seconds, "seconds")
