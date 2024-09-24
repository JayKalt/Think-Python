# Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!):

#	is_palindrome("abba")
#	not is_palindrome("abab")
#	is_palindrome("tenet")
#	not is_palindrome("banana")
#	is_palindrome("straw warts")
#	is_palindrome("a")
#	is_palindrome("")) # Is an empty string a palindrome?

def reverse(string):
	return string[::-1]


def is_palindrome(string):
	return string == string[::-1]

print(is_palindrome("abba"))
print(not is_palindrome("abab"))
print(is_palindrome("tenet"))
print(not is_palindrome("banana"))
print(is_palindrome("straw warts"))
print(is_palindrome("a"))
print(is_palindrome(""))
