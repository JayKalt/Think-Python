# Write the function f2c(t) designed to return the integer value of the nearest degree Celsius for given temper-
# ature in Fahrenheit. (hint: you may want to make use of the built-in function, round. Try printing round.
# __doc__ in a Python shell or looking up help for the round function, and experimenting with it until you are
# comfortable with how it works.)

# f2c(212) == 100	# Boiling point of water
# f2c(32) == 0		# Freezing point of water
# f2c(-40) == -40	# Wow, what an interesting case!
# f2c(36) == 2
# f2c(37) == 3
# f2c(38) == 3
# f2c(39) == 4

def f2c(t):
	"""
	  Returns the integer value of the nearest defree Celsius for given
	  temperature in Fahrenheit using the built-in function, round.
	"""

	return round((t - 32) / 1.8)


print(f2c(212) == 100)
print(f2c(32) == 0)
print(f2c(-40) == -40)
print(f2c(36) == 2)
print(f2c(37) == 3)
print(f2c(38) == 3)
print(f2c(39) == 4)
