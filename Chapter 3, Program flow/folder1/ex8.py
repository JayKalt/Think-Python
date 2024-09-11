# Write a program which, given the length of three sides of a triangle, will determine whether the triangle is right-
# angled.
# Assume that the third argument to the function is always the longest side.
# It will return True if the triangle is right-angled, or False otherwise.

print("Enter the sides of a triangle (longest for last): ")
side_a = int(input("Side a: "))
side_b = int(input("Side b: "))
long_side = int(input("Long side: "))

if(side_a ** 2 + side_b ** 2 == long_side ** 2):
	print("True")
else:
	print("False")
