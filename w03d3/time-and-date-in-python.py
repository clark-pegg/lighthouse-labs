from datetime import datetime, timedelta
import calendar

now = datetime.now()

# Part 1
print(now)
print(now.date().year)
print(now.date().month)
print(now.date().isocalendar().week)
print(now.date().strftime("%A"))
print(now.date().strftime("%j"))
print(now.date().day)
print(now.date().weekday() + 1)

# Part 2
string = 'Jan 1 2014 2:43PM'

then = datetime.strptime(string, "%b %d %Y %I:%M%p")

print(then)

# Part 3
print(now.time())

# Part 4
five_days_ago = now - timedelta(days=5)

print(five_days_ago)

# Part 5
unix = 1284105682

then = datetime.fromtimestamp(unix)

print(then)

# Part 6
print(now.date().strftime("%j"))

# Part 7
print(now.date().isocalendar().week)

# Part 8
date_a = datetime(2020,2,2)
date_b = datetime(2020,1,1)

print(date_a - date_b)

# Part 9
month = 10
year = 2016

num_days = calendar.monthrange(year, month)[1]

days = [datetime(year, month, day) for day in range(1, num_days+1)]

for day in days:
  print(day.date())

# Part 10
start_dt = datetime(2015, 12, 20)
end_dt = datetime(2016, 1, 11)

delta = end_dt - start_dt

for n in range(delta.days + 1):
  day = start_dt + timedelta(days = n)
  print(day.date())