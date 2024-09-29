# Now rewrite the count_letters function so that instead of traversing the string, it repeatedly calls the find
# method, with the optional third parameter to locate new occurrences of the letter being counted.

def count_letters(string, letter, end):
	"""
	  Exercise 3 but using find and the third parameter (ending parameter)
	"""
	count = 0
	start = 0

	while True:
#		start = string.find(letter, start, end)
#		if start == -1:
		if string.find(letter, start, end) == -1:
			break
		count += 1
#		start += 1
		start = string.find(letter, start, end) + 1

	return count


def count_letters2(string, letter, end):
	"""
	  Second version
	"""
	count = 0
	start = 0

	while True:
#		start = string.find(letter)
#		if start == -1:
		if string.find(letter, start, end) == -1:
			break
		string = string[string.find(letter, start, end) + 1:end]
		count += 1

	return count

#def count_letter2(string, letter, end):

# Test made by GPT-4o

def test_count_letters():
    # Test cases
    assert count_letters("hello world", "o", 11) == 2, "Test Case 1 Failed"
    assert count_letters("hello world", "l", 11) == 3, "Test Case 2 Failed"
    assert count_letters("hello world", "h", 11) == 1, "Test Case 3 Failed"
    assert count_letters("hello world", "z", 11) == 0, "Test Case 4 Failed"
    assert count_letters("", "a", 0) == 0, "Test Case 5 Failed"  # Empty string
    assert count_letters("abcabcabc", "a", 9) == 3, "Test Case 6 Failed"  # Multiple occurrences
    assert count_letters("abcabcabc", "b", 9) == 3, "Test Case 7 Failed"  # Multiple occurrences
    assert count_letters("abcabcabc", "c", 9) == 3, "Test Case 8 Failed"  # Multiple occurrences
    assert count_letters("abcabcabc", "d", 9) == 0, "Test Case 9 Failed"  # No occurrences
    assert count_letters("a" * 1000, "a", 1000) == 1000, "Test Case 10 Failed"  # Long string

    print("All test cases passed!")


def test_count_letters2():
    # Test cases
    assert count_letters2("hello world", "o", 11) == 2, "Test Case 1 Failed"
    assert count_letters2("hello world", "l", 11) == 3, "Test Case 2 Failed"
    assert count_letters2("hello world", "h", 11) == 1, "Test Case 3 Failed"
    assert count_letters2("hello world", "z", 11) == 0, "Test Case 4 Failed"
    assert count_letters2("", "a", 0) == 0, "Test Case 5 Failed"  # Empty string
    assert count_letters2("abcabcabc", "a", 9) == 3, "Test Case 6 Failed"  # Multiple occurrences
    assert count_letters2("abcabcabc", "b", 9) == 3, "Test Case 7 Failed"  # Multiple occurrences
    assert count_letters2("abcabcabc", "c", 9) == 3, "Test Case 8 Failed"  # Multiple occurrences
    assert count_letters2("abcabcabc", "d", 9) == 0, "Test Case 9 Failed"  # No occurrences
    assert count_letters2("a" * 1000, "a", 1000) == 1000, "Test Case 10 Failed"  # Long string

    print("All test cases passed!")


# Run the tests
test_count_letters()
test_count_letters2()
