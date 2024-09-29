# Write a function that reverses its string argument, and satisfies these tests:

def reverse(string):
	return string[::-1]


# Write a function that mirrors its argument:

def mirror(string):
	return string + reverse(string)




print("Exercise 7", end="\n\n")
print(reverse("happy") == "yppah")
print(reverse("Python") == "nohtyP")
print(reverse("") == "")
print(reverse("a") == "a")

print("Exercise 8")
print(mirror("good") == "gooddoog")
print(mirror("Python") == "PythonnohtyP")
print(mirror("") == "")
print(mirror("a") == "aa")
