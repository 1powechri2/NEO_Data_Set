from datetime import datetime, timedelta

start_date = datetime(2019, 1, 1)
end_date   = start_date + timedelta(1)

print(start_date.strftime('%Y-%m-%d'))
print(end_date.strftime('%Y-%m-%d'))

start_date = end_date
end_date   = start_date + timedelta(1)

print(start_date.strftime('%Y-%m-%d'))
print(end_date.strftime('%Y-%m-%d'))
