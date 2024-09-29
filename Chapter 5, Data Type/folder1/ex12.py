# Write a function that removes the first occurrence of a string from another string:

#	remove("an", "banana") == "bana"
#	remove("cyc", "bicycle") == "bile"
#	remove("iss", "Mississippi") == "Missippi"
#	remove("eggs", "bicycle") == "bicycle"


def remove(substr, str):
	if substr in str:
		return str[:str.find(substr)] + str[str.find(substr) + len(substr):]
	return str

print(remove("an", "banana") == "bana")
print(remove("cyc", "bicycle") == "bile")
print(remove("iss", "Mississippi") == "Missippi")
print(remove("eggs", "bicycle") == "bicycle")
