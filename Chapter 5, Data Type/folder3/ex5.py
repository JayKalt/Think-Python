# Lists can be used to represent mathematical vectors. In this exercise and several that follow you will write
# functions to perform standard operations on vectors. Create a script named vectors.py and write Python
# code to pass the tests in each case.

# Write a function add_vectors(vector1,vector2) that takes two lists of numbers of the same length,
# and returns a new list containing the sums of the corresponding elements of each:

#	add_vectors([1, 1], [1, 1]) == [2, 2]
#	add_vectors([1, 2], [1, 4]) == [2, 6]
#	add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4]


def add_vectors(vector1, vector2):
	new_vector = vector1[:]
	for i, value in enumerate(vector2):
		new_vector[i] += value

	return new_vector


print(add_vectors([1, 1], [1, 1]) == [2, 2])
print(add_vectors([1, 2], [1, 4]) == [2, 6])
print(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

