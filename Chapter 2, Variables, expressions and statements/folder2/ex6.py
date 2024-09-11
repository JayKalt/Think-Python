# Evaluate the following numerical expressions in your head, then use the Python interpreter to check your results:

#	1. >>> 5 % 2
#	2. >>> 9 % 5
#	3. >>> 15 % 12
#	4. >>> 12 % 15
#	5. >>> 6 % 6
#	6. >>> 0 % 7
#	7. >>> 7 % 0

# What happened with the last example? Why? If you were able to correctly anticipate the computer’s response
# in all but the last one, it is time to move on. If not, take time now to make up examples of your own.
# Explore the modulus operator until you are confident you understand how it works

# Solution:

#	1. >>> 1
#	1. >>> 4
#	1. >>> 3
#	1. >>> 12
#	1. >>> 0
#	1. >>> 0
#	1. >>> Error

# If A > B then the module is the difference between A and n-times B as long as n-times B <= A
# If A < B then the module is the dividend beacuse it's impossible to divide by a greater number and get a positive remainder
# If A = B then the module is 0 because there is no remainder by the division
# If A = 0 then the module is 0 because there is no remainder from any division by a non-zero number
# If B = 0 then the module is an error because it's impossible to divide a number by zero and so to have a remainder
