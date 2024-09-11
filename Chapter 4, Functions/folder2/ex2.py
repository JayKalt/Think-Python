# Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assume day 0 is
# “Sunday”. Once again, return None if the arguments to the function are not valid

def day_name(day_number):
	"""
	  Returns the day name from the given day number (0 to 6)
	  Returns None if the day number is invalid
	"""

	week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

	if day_number in range(len(week)):
		return week[day_number]
	return None


print(day_name(7))
