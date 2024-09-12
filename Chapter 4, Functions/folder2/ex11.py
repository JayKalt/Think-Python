# Write a compare function that returns 1 if a > b, 0 if a == b, and -1 if a < b

# compare(5, 4) == 1
# compare(7, 7) == 0
# compare(2, 3) == -1
# compare(42, 1) == 1

def compare(a, b):
	"""
	  Compares a and b and returns:
		1 if a > b
		0 if a == b
		-1 if a < b
	"""

	if a > b:
		return 1
	elif a == b:
		return 0
	return -1


print(compare(5, 4) == 1)
print(compare(7, 7) == 0)
print(compare(2, 3) == -1)
print(compare(42, 1) == 1)