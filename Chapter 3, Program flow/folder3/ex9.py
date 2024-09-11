# Write a program which prints True when n is a prime number and False otherwise.

n = int(input("Enter an integer: "))

if n <= 1:
	print(False)
else:
	is_prime = True
	if n == 2:
		is_prim = True
	elif n % 2 == 0:
		is_prime = False
	else:
		div = 3
		while div * 2 <= n:
			if n % div == 0:
				is_prime = False
				break
			div += 1
	print(is_prime)
