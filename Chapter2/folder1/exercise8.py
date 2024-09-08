# Write a Python program to solve the general version of the above problem.
# Ask the user for the time now (in hours), and ask for the number of hours to wait.
# Your program should output what the time will be on the clock when the alarm goes off.

current_time = int(input("What time is it? "))
to_wait = int(input("How many hours before the alarm goes off? "))

print("The alarm goes off at", (current_time + to_wait) % 24)
