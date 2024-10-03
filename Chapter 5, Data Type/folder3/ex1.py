# What is the Python interpreter’s response to the following?

#	>>> list(range(10, 0, -2))

# The three arguments to the range function are start, stop, and step, respectively. In this example, start is
# greater than stop. What happens if start < stop and step < 0? Write a rule for the relationships
# among start, stop, and step.


# Answer:

#	[10, 8, 6, 4, 2]

# RULE:

#	Forward default : list(range(10))
#	Forward step    : list(range(10, 2))

#	Backward default: list(range(10, 0, -1))
#	Backward step   : list(range(10, 0, -2))
