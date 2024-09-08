# Write a program that prints out the first n triangular numbers.
# A call to with n = 5 would produce the following output:

# 1	1
# 2	3
# 3	6
# 4	10
# 5	15

# (hint: use a web search to find out what a triangular number is.)


sum = 0
for i in range(1, 6):
	sum += i
	print(i, sum)
