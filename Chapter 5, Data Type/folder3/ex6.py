# Write a function scalar_mult(scalar, vector) that takes a number, scalar, and a list, vector
# and returns the scalar multiple of vector by scalar. :

#	scalar_mult(5, [1, 2]) == [5, 10]
#	scalar_mult(3, [1, 0, -1]) == [3, 0, -3]
#	scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14]


def scalar_mult(scalar, vector):
	for i, _ in enumerate(vector):
		vector[i] *= scalar

	return vector


print(scalar_mult(5, [1, 2]) == [5, 10])
print(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
print(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
