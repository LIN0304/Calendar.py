import calendar
def printcalender(year):
    print(calendar.calendar(year))
year=int(input('Enter the year'))
mm=int(input('Enter the month'))
print(calendar.month(year, mm))
printcalender(year)