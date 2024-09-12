# Extend to_secs so that it can cope with real values as inputs. It should always return an integer number of
# seconds (truncated towards zero):

# to_secs(2.5, 0, 10.71) == 9010
# to_secs(2.433,0,0) == 8758

def to_secs(h, m, s):
	"""
	  Converts hours, minutes and seconds to a total number of seconds.

	  Float values are allowed.
	  Returns an integer number of seconds (truncated towards zero)
	"""

	return int(h * 60 ** 2) + int(m * 60) + int(s)


print(to_secs(2.5, 0, 10.71) == 9010)
print(to_secs(2.433,0,0) == 8758)
