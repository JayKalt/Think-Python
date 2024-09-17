# Write a function is_factor(f, n) that passes these tests:

# is_factor(3, 12)
# not is_factor(5, 12)
# is_factor(7, 14)
# not is_factor(7, 15)
# is_factor(1, 15)
# is_factor(15, 15)
# not is_factor(25, 15)


def is_factor(f, n):
	"""
	  Returns Ture if is fractor, else False
	"""

	return n % f == 0


print(is_factor(3, 12))
print(not is_factor(5, 12))
print(is_factor(7, 14))
print(not is_factor(7, 15))
print(is_factor(1, 15))
print(is_factor(15, 15))
print(not is_factor(25, 15))


# Write is_multiple to satisfy these statements using is_factor from the previous execise.
# is_multiple(12, 3) is_multiple(12, 4) not is_multiple(12, 5) is_multiple(12, 6) not is_multiple(12, 7)

def is_multiple(n, f):
	"""
	  Returns True if is multiple, else Flase
	"""

	is_fracotr(f, n)


print(is_multiple(12, 3))
print(is_multiple(12, 4))
print(not is_multiple(12, 5))
print(is_multiple(12, 6))
print(not is_multiple(12, 7))
