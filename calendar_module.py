import calendar

month, day, year = map(int, input().split())
weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

print(weekdays[calendar.weekday(year, month, day)])
