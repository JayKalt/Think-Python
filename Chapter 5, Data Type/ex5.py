# Assign to a variable in your program a triple-quoted string that contains your favourite paragraph of text —
# perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.
# Write a function which removes all punctuation from the string, breaks the string into a list of words, and counts
# the number of words in your text that contain the letter “e”. Your program should print an analysis of the text
# like this:

#	Your text contains 243 words, of which 109 (44.8%) contain an "e".

import string

def remove_punct(text):
	count = 0
	text_sans_punct = ""

	for letter in text:
		if letter not in string.punctuation:
			text_sans_punct += letter

	return text_sans_punct.split()


def count_e_in(text):
	count = 0

	for word in text:
		if 'e' in word:
			count += 1

	return count

smokey_quotes = """“The older I get, the more I realize that the greatest
reward in life comes from pushing yourself to the limits and chasing your dreams.”

“Drifting is not just about speed and precision, it’s about the art of controlling
chaos and finding harmony in motion.”

“The road to success is not a smooth ride, but it’s the bumps and curves that make
the journey worthwhile.”

“In the world of drifting, perfection is not the goal, it’s the pursuit of perfection
that keeps us coming back for more.”

“The sound of tires screeching, the smell of burning rubber, and the feeling of
adrenaline coursing through your veins, that’s what drifting is all about.”"""


smokey_cleared = remove_punct(smokey_quotes)
words_count = len(smokey_cleared)
e_in_words = count_e_in(smokey_cleared)

print('''Your text contains {0} words, of which {1} ({2:.2f}%) contain an "e".'''.format( words_count, e_in_words, e_in_words/words_count * 100))
