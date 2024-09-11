# Add a print function to Newton’s sqrt algorithm that prints out better each time it is calculated. Call your
# modified program with 25 as an argument and record the results.

n = 25
threshold = 0.001
approximation = n/2

# Start with some or other guess at the answer
while True:
	better = (approximation + n/approximation)/2
	if abs(approximation - better) < threshold:
		break
	print(better)
	approximation = better
