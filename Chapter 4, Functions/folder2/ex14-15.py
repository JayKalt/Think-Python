# Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is
# an even number and False if it is odd.
# Add your own tests to the test suite

def is_even(n):
	"""
	  Takes an integer as an argument and returns:
		True  if the argument is an even number
		False if the argument is an ood number
	"""
	return n % 2 == 0


print("is_even(test)")
print(is_even(12) == True)
print(is_even(7) == False)
print(is_even(0) == True)
print(is_even(-3) == False)
print(is_even(-4) == True)


# Now write the function is_odd(n) that returns True when n is odd and False otherwise. Include unit tests
# for this function too.
# Finally, modify it so that it uses a call to is_even to determine if its argument is an odd integer, and ensure
# that its test still pass.

def is_odd(n):
	"""
	  Takes an integer as an argument and returns:
		True  if the argument is an even number
		False if the argument is an ood number
	"""
	return not(is_even(n))


print("is_odd(test)")
print(is_odd(12) != True)
print(is_odd(7) != False)
print(is_odd(0) != True)
print(is_odd(-3) != False)
print(is_odd(-4) != True)
