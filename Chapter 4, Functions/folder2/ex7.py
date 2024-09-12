# Write a function to_secs that converts hours, minutes and seconds to a total number of seconds. Here are
# some tests that should pass:

# to_secs(2, 30, 10) == 9010
# to_secs(2, 0, 0) == 7200
# to_secs(0, 2, 0) == 120
# to_secs(0, 0, 42) == 42
# to_secs(0, -10, 10) == -590

def to_secs(h, m, s):
	"""
	  Converts and returns hours, minutes and seconds to a total number of seconds
	"""

	return (h * 60 ** 2) + (m * 60) + s


print(to_secs(2, 30, 10) == 9010)
print(to_secs(2, 0, 0) == 7200)
print(to_secs(0, 2, 0) == 120)
print(to_secs(0, 0, 42) == 42)
print(to_secs(0, -10, 10) == -590)
