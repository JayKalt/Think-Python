# Write a function called hypotenuse that returns the length of the hypotenuse of a right triangle given the
# lengths of the two legs as parameters:

# hypotenuse(3, 4) == 5.0
# hypotenuse(12, 5) == 13.0
# hypotenuse(24, 7) == 25.0
# hypotenuse(9, 12) == 15.0

import math

def hypotenuse(a, b):
	"""
	  Returns the lenght of the hypotenuse of a right trianlge given the lenghts
	  of the two legs as parameters
	"""

	return math.sqrt(math.pow(a, 2) + math.pow(b, 2))


print(hypotenuse(3, 4) == 5.0)
print(hypotenuse(12, 5) == 13.0)
print(hypotenuse(24, 7) == 25.0)
print(hypotenuse(9, 12) == 15.0)
