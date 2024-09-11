# Write a program which is given an exam mark, and it returns a string — the grade for that mark — according to
# this scheme:

# Mark		Grade

#  >= 75 	First
# [70-75)	Upper Second
# [60-70) 	Second
# [50-60) 	Third
# [45-50) 	F1 Supp
# [40-45) 	F2
#  < 40 	F3


scheme = [(75, "First"),
		  (70, "Upper second"),
		  (60, "Second"),
		  (50, "Third"),
		  (45, "F1 Supp"),
		  (40, "F2"),
		  (0 , "F3")]

numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]


for mark in numbers:
	for boundary, grade in scheme:
		if mark >= boundary:
			print("Student grade:", grade)
			break
