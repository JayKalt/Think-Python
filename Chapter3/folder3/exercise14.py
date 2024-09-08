# Write a program that computes the sum of the squares of the numbers in the list numbers. For example a call
# with, numbers = [2, 3, 4] should print 4+9+16 which is 29.


numbers = [2, 3, 4]
sum = 0

for number in numbers:
	sum += number ** 2

print(sum)
