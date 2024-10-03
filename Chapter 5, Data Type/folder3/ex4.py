# What will be the output of the following program?

#	this = ["I", "am", "not", "a", "crook"]
#	that = ["I", "am", "not", "a", "crook"]
#	print("Test 1: {0}".format(this is that))
#	that = this
#	print("Test 2: {0}".format(this is that))

# Provide a detailed explanation of the results


# ANSWER:
# "Test 1: False"
# "Test 2: True"

# Test 1
# In this case we create 2 different lists, "this" and "that". Even if the items of the lists
# are the same, that doesn't mean the list "this" it's "that".

# Test 2
# By assigning "that" to "this", I'm now creating an alias that referes to the same object.

