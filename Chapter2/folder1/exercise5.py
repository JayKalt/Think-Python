# The formula for computing the final amount if one is earning compound interest is given on Wikipedia as:

#	A = P (1 + r/n)^nt
#	Where:
#	- P = principal amount (initial investment)
#	- r = annual nominal interest rate (as a decimal)
#	- n = number of times the interest is compunded per year
#	- t = number of years

# Here, P is the principal amount (the amount that the interest is provided on), n the frequency that the interest
# is paid out (per year), and r the interest rate. The number of years that the interest is calculated for is t.
# Write a program that replaces these letters with something a bit more human-readable, and calculate the interest for
# some varying amounts of money at realistic interest rates such as 1%, and -0.05%.
# When you have that working, ask the user for the value of some of these variables and do the calculation.

P = int(input("Please enter your initial investment: "))
t = int(input("Please enter the number of years: "))

print("The final ammount will be of", P * ((1 + -0.05/1)**(-0.05*t)), "$")
