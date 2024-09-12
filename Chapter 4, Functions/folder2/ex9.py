# Write three functions that are the “inverses” of to_secs:

# 1. hours_in returns the whole integer number of hours represented by a total number of seconds.

# 2. minutes_in returns the whole integer number of left over minutes in a total number of seconds, once
#    the hours have been taken out.

# 3. seconds_in returns the left over seconds represented by a total number of seconds.


# You may assume that the total number of seconds passed to these functions is an integer. Here are some test
# cases:

#       hours_in(9010) == 2
#       minutes_in(9010) == 30
#       seconds_in(9010) == 10


def hours_in(total_sec):
	"""
	Returns the whole integer number of hours represented by a total number of seconds.
	"""
	return total_sec // 3600

def minutes_in(total_sec):
	"""
	Returns the whole integer number of leftover minutes in a total number of seconds, once the hours have been taken out.
	"""
	return (total_sec % 3600) // 60

def seconds_in(total_sec):
	"""
	Returns the leftover seconds represented by a total number of seconds.
	"""
	return total_sec % 60



print(hours_in(9010))
print(minutes_in(9010))
print(seconds_in(9010))
