# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday.
# Write a program that asks a day number, and prints the day name (a string).


week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day = int(input("Enter a day of the week (from 0 (Sunday) to 6 (Staturday)): "))

print("The day you entered is:", week[day])
