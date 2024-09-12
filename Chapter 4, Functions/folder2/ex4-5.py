# Write a function that helps answer questions like ‘“Today is Wednesday. I leave on holiday in 19 days time.
# What day will that be?”’ So the function must take a day name and a delta argument — the number of days
# to add — and should return the resulting day name:

# day_add("Monday", 4) == "Friday"
# day_add("Tuesday", 0) == "Tuesday"
# day_add("Tuesday", 14) == "Tuesday"
# day_add("Sunday", 100) == "Tuesday"

# Hint: use the first two functions written above to help you write this one

def day_name(day_number):
	"""
	  Returns the day name from the given day number (0 to 6)
	  Returns None if the day number is invalid
	"""

	week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

	if day_number in range(len(week)):
		return week[day_number]
	return None


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


def day_add(day, to_add):
	"""
	  Returns the name of the day you'll leave given the current day name
	  and the number of days to add
	"""

	return day_name((day_num(day) + to_add) % 7)


print(day_add("Monday", 4) == "Friday")
print(day_add("Tuesday", 0) == "Tuesday")
print(day_add("Tuesday", 14) == "Tuesday")
print(day_add("Sunday", 100) == "Tuesday")


# Can your day_add function already work with negative deltas? For example, -1 would be yesterday, or -7
# would be a week ago:

# day_add("Sunday", -1) == "Saturday"
# day_add("Sunday", -7) == "Sunday"
# day_add("Tuesday", -100) == "Sunday"

# If your function already works, explain why. If it does not work, make it work.
# Hint: Play with some cases of using the modulus function % (introduced at the beginning of the previous
# chapter). Specifically, explore what happens to x % 7 when x is negative.

print(day_add("Sunday", -1) == "Saturday")
print(day_add("Sunday", -7) == "Sunday")
print(day_add("Tuesday", -100) == "Sunday")


# Explanatino:

# My function works cause it use the module operator.
# Because when the divisor is negative the remainder of the division will
# always going to be the difference between the dividend and divisor