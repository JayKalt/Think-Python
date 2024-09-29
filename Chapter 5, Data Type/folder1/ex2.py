# Modify:

#	prefixes = "JKLMNOPQ"
#	suffix = "ack"
#
#	for letter in prefixes:
#		print(letter + suffix)

# so that Ouack and Quack are spelled correctly.


prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
	modified_letter = letter + ('u' if letter in 'OQ' else '')
	print(letter + suffix)


# made with the help of gpt-4o (mine was more of a C-style solution)
# that is so cool tbh
