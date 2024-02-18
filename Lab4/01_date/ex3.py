'''
Write a Python program to drop microseconds from datetime.
'''
import datetime


dt_with_microseconds = datetime.datetime(2024, 2, 18, 12, 34, 56, 789)
dt_without_microseconds = dt_with_microseconds.replace(microsecond=0)

print("Date and time with microseconds", dt_with_microseconds)
print("Date and time without microseconds:", dt_without_microseconds)