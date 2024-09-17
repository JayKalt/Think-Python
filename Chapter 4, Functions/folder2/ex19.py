# Now do the opposite: write the function c2f which converts Celsius to Fahrenheit:

# c2f(0) == 32
# c2f(100) == 212
# c2f(-40) == -40
# c2f(12) == 54
# c2f(18) == 64
# c2f(-48) == -54


def c2f(t):
	"""
	  Returns the integer value of the nearest defree Fahrenheit for given
	  temperature in Celsius using the built-in function, round.
	"""

	return round((t * 1.8) + 32)


print(c2f(0) == 32)
print(c2f(100) == 212)
print(c2f(-40) == -40)
print(c2f(12) == 54)
print(c2f(18) == 64)
print(c2f(-48) == -54)
