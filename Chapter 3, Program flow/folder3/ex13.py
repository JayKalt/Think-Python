# Write a program that counts the number of even digits in n.

n = int(input("Enter n: "))
count = 0

while n > 0:
	if (n % 10) % 2 == 0:
		count += 1
	n //= 10

print(count)
