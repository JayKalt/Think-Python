# The four compass points can be abbreviated by single-letter strings as “N”, “E”, “S”, and “W”. Write a function
# turn_clockwise that takes one of these four compass points as its parameter, and returns the next compass
# point in the clockwise direction. Here are some tests that should pass:

# >>>turn_clockwise("N") == "E"
# True
# >>>turn_clockwise("W") == "N"
# True

# You might ask “What if the argument to the function is some other value?” For all other cases, the function
# should return the value None.


def turn_clockwise(compass_point):
	"""
	  Returns the next compass point in the clockwise direction
	"""

	if compass_point == "N":
		return "E"
	elif compass_point == "E":
		return "S"
	elif compass_point == "S":
		return "W"
	elif compass_point == "W":
		return "N"
	else:
		return None

print(turn_clockwise("N"))
