# Write the inverse function day_num which is given a day name, and returns its number.
# Once again, if this function is given an invalid argument, it should return None

def day_num(day_name):
	"""
	  Returns the day name from the given day number (0 to 6)
	  Returns None if the day number is invalid
	"""

	week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

	if day_name in week:
		for i in range(len(week)):
			if day_name == week[i]:
				return i
	return None


print(day_num("Tuesday"))
