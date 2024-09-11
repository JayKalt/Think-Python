# Write a program which, given the length of two sides of a right-angled triangle, returns the length of the hy-
# potenuse. (Hint: x ** 0.5 will return the square root.)

lenght_a = int(input("Enter first side of the right-angled triangle: "))
lenght_b = int(input("Enter second side of the right-angled triangle: "))

print("The hypotenuse is", (lenght_a ** 2 + lenght_b ** 2) ** 0.5)
