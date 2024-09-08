# 1. Write a program to count how many odd numbers are in a list

list1 = [4, 2, 1, 6]
count = 0

for number in list1:
	if(number % 2 != 0):
		count += 1

print("#odd:", count)


# 2. Sum up all the even numbers in a list.

list2 = [0, 1, 3, 5]
sum = 0

for number in list1:
	if(number % 2 == 0):
		sum += number

print("sum even:", sum)


# 3. Sum up all the negative numbers in a list.

list3 = [-1, -4, -10, 14]
sum = 0

for number in list3:
	if(number < 0):
		sum += number

print("sum negative:", sum)


# 4. Count how many words in a list have length 5

list4 = ["The", "word", "world", "has", "five", "letters"]
count = 0

for word in list4:
	ch_count = 0
	for letters in word:
		ch_count += 1
	if(ch_count == 5):
		count += 1

print("length 5:", count)


# 5. Sum all the elements in a list up to but not including the first even number. (What if there is no even number?)

list5 = [1, 3, 5, 6, 7, 11]
count = 0
index = 0

while index < len(list5) and list5[index] % 2 != 0:
	count += list5[index]
	index += 1

print("sum till first even:", count)


# 6. Count how many words occur in a list up to and including the first occurrence of the word “sam”.
# (What if “sam” does not occur?)

list6 = ["hi", "red", "tube", "sam", "test"]
count = 0
index = 0

while index < len(list6) and list6[index] != "sam":
	count += 1
	index += 1

print("words till first sam:", count)
