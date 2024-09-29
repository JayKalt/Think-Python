# Encapsulate

#	word = "banana"
#	count = 0
#
#	for letter in word:
#		if letter == "a":
#			count += 1
#	print(count)

# in a function named count_letters, and generalize it so that it accepts the string and the letter as arguments.
# Make the function return the number of characters, rather than print the answer. The caller should do the printing.


def count_letters(string, letter):
	"""
	  Returns the number of characters, given the string and the letter to count
	"""

	count = 0

	for ch in string:
		if letter == ch:
			count += 1
	return count


print(count_letters("banana", 'a'))
