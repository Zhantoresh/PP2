'''
Write a Python program to print yesterday, today, tomorrow.
'''

import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print("today:", today)
print("yesterday:", yesterday)
print("tomorrow:", tomorrow)