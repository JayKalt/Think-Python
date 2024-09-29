# Write a function that removes all occurrences of a given letter from a string:

#	remove_letter("a", "apple") == "pple"
#	remove_letter("a", "banana") == "bnn"
#	remove_letter("z", "banana") == "banana"
#	remove_letter("i", "Mississippi") == "Msssspp"
#	remove_letter("b", "") = ""
#	remove_letter("b", "c") = "c"


# Solution 1
def remove_letter(letter, string):
	while letter in string:
		string = string[:string.find(letter)] + string[string.find(letter) + 1:]

	return string


# Solution 2
def remove_letter2(letter, string):
	while True:
		if string.find(letter) == -1:
			break
		string = string[:string.find(letter)] + string[string.find(letter) + 1:]

	return string

print("remove_letter test")
print(remove_letter("a", "apple") == "pple")
print(remove_letter("a", "banana") == "bnn")
print(remove_letter("z", "banana") == "banana")
print(remove_letter("i", "Mississippi") == "Msssspp")
print(remove_letter("b", "") == "")
print(remove_letter("b", "c") == "c")

print()
print("remove_letter2 test")
print(remove_letter2("a", "apple") == "pple")
print(remove_letter2("a", "banana") == "bnn")
print(remove_letter2("z", "banana") == "banana")
print(remove_letter2("i", "Mississippi") == "Msssspp")
print(remove_letter2("b", "") == "")
print(remove_letter2("b", "c") == "c")
