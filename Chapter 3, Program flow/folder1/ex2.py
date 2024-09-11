# You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3
# (a Wednesday). You return home after 137 sleeps. Write a general version of the program which asks for the
# starting day number, and the length of your stay, and it will tell you the name of day of the week you will return on.

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

starting_day_number = int(input("What's your starting day number? "))
lenght_of_stay = int(input("How long will last your holiday? "))

print("You'll be back on a", week[(starting_day_number + lenght_of_stay) % 6])
