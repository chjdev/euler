# Counting Sundays
# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from itertools import takewhile


def next_day(date=(0, 'Monday', 0, 1900)):
    day_strings = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    next_day_string = {day_strings[d % 7]: day_strings[(d + 1) % 7] for d in range(0, 7)}
    days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    while True:  # no tail recursion in python :(
        day, day_string, month, year = date
        offset = 1 if month == 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 0
        month_boundary = days_in_month[month] + offset
        new_day = (day + 1) % month_boundary
        new_month = (month + 1) % 12 if new_day == 0 else month
        new_year = year + 1 if new_day == 0 and new_month == 0 else year

        new_date = (new_day, next_day_string[day_string], new_month, new_year)
        yield new_date
        date = new_date

sundays_on_first = filter(lambda day: day[0] == 0 and day[1] == 'Sunday', next_day())
from_1901 = filter(lambda day: day[3] > 1900, sundays_on_first)
until_2001 = takewhile(lambda day: day[3] < 2001, from_1901)
print(len(list(until_2001)))
