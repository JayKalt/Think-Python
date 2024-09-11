# Recall the digit counting program. What will it print with n = 0? Modify it to print 1 for this case. Why does
# a call with n = -24 result in an infinite loop? (hint: -1//10 evaluates to -1) Modify num_digits so that it
# works correctly with any integer value.


n = int(input("Enter integer value: "))
count = 0

if n == 0:
	count += 1
elif n < 0:
	n = -n

while n != 0:
	count += 1
	n = n // 10

print(count)
