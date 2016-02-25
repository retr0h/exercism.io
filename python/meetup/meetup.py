import calendar
from datetime import date

DOW_INDEX = [d for d in calendar.day_name]


def meetup_day(year, month, weekday, occurance):
    day_index = DOW_INDEX.index(weekday)
    dates = [
        week[day_index]
        for week in calendar.monthcalendar(year, month) if week[day_index]
    ]

    if occurance == '1st':
        day_index = 0
    elif occurance == '2nd':
        day_index = 1
    elif occurance == '3rd':
        day_index = 2
    elif occurance == '4th':
        day_index = 3
    elif occurance == '5th':
        day_index = 4
    elif occurance == 'last':
        day_index = -1
    elif occurance == 'teenth':
        print dates
        for day in dates:
            if 13 <= day <= 19:
                return date(year, month, day)

    return date(year, month, dates[day_index])
