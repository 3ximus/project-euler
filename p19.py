first_sunday = 6 # first sunday
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_sunday(d):
	return d % 7 == first_sunday

def month_days(m, y):
	if m == 2 and y % 4 == 0: # year 2000 is divisible by 400 so it is a leap year
		return month[m-1] + 1
	return month[m-1]

total_days = 0
total_sundays = 0
for y in range(1901, 2001):
	for m in range(1,13):
		total_days += month_days(m, y)
		if is_sunday(total_days + 1): # check 1st day of next month
			total_sundays += 1
print(total_sundays)




