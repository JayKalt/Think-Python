# Write a function that removes all occurrences of a string from another string:

#	remove_all("an", "banana") == "ba"
#	remove_all("cyc", "bicycle") == "bile"
#	remove_all("iss", "Mississippi") == "Mippi"
#	remove_all("eggs", "bicycle") == "bicycle"


def remove(substr, str):
	if substr in str:
		return str[:str.find(substr)] + str[str.find(substr) + len(substr):]
	return str

def remove_all(substr, str):
	while substr in str:
		str = remove(substr, str)
	return str


print(remove_all("an", "banana") == "ba")
print(remove_all("cyc", "bicycle") == "bile")
print(remove_all("iss", "Mississippi") == "Mippi")
print(remove_all("eggs", "bicycle") == "bicycle")
