# Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to and including n. So
# sum_to(10) would be 1+2+3. . . +10 which would return the value 55.

def sum_to(n):
	"""
	  Returns the sum of all integer numbers up to and including n
	  with given n
	"""
	return n * (n * 1) // 2

print(sum_to(10))
