'''
Write a Python program to subtract five days from current date.
'''

import datetime
today = datetime.datetime.now()
print("Five days ago:", today - datetime.timedelta(days=5))