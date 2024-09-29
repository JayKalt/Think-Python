# Write a function that counts how many times a substring occurs in a string:

#	count("is", "Mississippi") == 2
#	count("an", "banana") == 2
#	count("ana", "banana") == 2
#	count("nana", "banana") == 1
#	count("nanan", "banana") == 0
#	count("aaa", "aaaaaa") == 4


def count(substr, str):
	count = 0

	while substr in str:
		count += 1
		str = str[str.find(substr) + 1:]

	return count

print(count("is", "Mississippi") == 2)
print(count("an", "banana") == 2)
print(count("ana", "banana") == 2)
print(count("nana", "banana") == 1)
print(count("nanan", "banana") == 0)
print(count("aaa", "aaaaaa") == 4)
