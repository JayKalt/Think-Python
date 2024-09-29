# We’ve said nothing in this chapter about whether you can pass tuples as arguments to a function.
# Construct a small Python example to test whether this is possible, and write up your findings

def operation(elements):
	(a, b, sign) = elements
	if sign == '+':
		return a + b
	elif sign == '-':
		return a - b
	elif sign == '*':
		return a * b
	elif sign == '/':
		return a / b
	else:
		return "Sign error"


elements = (5, 7, "+")
print(operation(elements) == 12)
elements = (5, 7, "*")
print(operation(elements) == 35)
elements = (5, 7, "%")
print(operation(elements) == "Sign error")

