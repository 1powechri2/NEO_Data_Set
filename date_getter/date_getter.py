import calendar as cal

new_cal = cal.Calendar()

month = 1
year  = 2019

dates = new_cal.itermonthdates(year, month)

date_list = []

for date in dates:
    if date.month == month:
        date_list.append(date.strftime('%Y-%m-%d'))

print(date_list)
