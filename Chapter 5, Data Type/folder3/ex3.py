# Draw a state snapshot for a and b before and after the third line of the following Python code is executed:

#	a = [1, 2, 3]
#	b = a[:]
#	b[0] = 5


# BEFORE:
#	a = [1, 2 ,3]
#	b = [1, 2, 3]

# AFTER:
#	a = [1, 2, 3]
#	b = [5, 2, 3]
