# Write a function days_in_month which takes the name of a month, and returns the number of days in the
# month. Ignore leap years:

# days_in_month("February") == 28
# days_in_month("December") == 31

# If the function is given invalid arguments, it should return None.

def days_in_month(month_name):
	"""
	  Returns the number of days in the month (ignores leap years)
	"""

	year = [("January", 31), ("February", 28), ("March", 31), ("April", 30),
		("May", 31), ("June", 30), ("July", 31), ("Agusut", 31),
		("Septermber", 30), ("October", 31), ("November", 30), ("December", 31)]

	for month, days in year:
		if month == month_name:
			return days
	return None


print(days_in_month("February"))
print(days_in_month("December"))
print(days_in_month("Decembre"))
