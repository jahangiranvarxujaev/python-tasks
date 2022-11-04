def get_days(month, year):
    days31 = [1, 3, 5, 7, 8, 10, 12]
    if month == 2:
        if (year % 4 == 0) and ((year % 400 == 0) or (year % 100 == 0)):
            return 29
        else:
            return 28
    elif month in days31:
        return 31
    else:
        return 30



#def make_calender(years):
#
#    for year in range(min(years), max(years)):
#        calender = []
#        calender.append(year)
#        for month in range(1, 12):
#            calender.append(month)
#            for day in range(1, 31):
#
#                days = get_days(month, year)
#                calender.append(days)
#                print(calender)
#                calender.remove(calender[2])
#            calender.remove(calender[1])
#        calender.remove(calender[0])

def make_calendar(from_year):
    calender = [[0, 0, 0]]
    counter =  0
    weekcode = 1
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for year in from_year:
        for month in range(1, 13):

            day_range = get_days(month, year)

            for day in range(1, day_range + 1):
                calender.append([year, month, day])
        for y in months:
            weekcode = (weekcode + y) % 7
            if (weekcode == 0) and (year > 1990):
                counter += 1






    return calender and counter





users_option1 = list(map(int, input().split()))
# users_option2 = int(input())
# print(get_days(users_option2))
print(make_calendar(users_option1))
