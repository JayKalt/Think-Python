# Revisit the drunk pirate problem. This time, the drunk pirate makes a turn, and then takes some steps forward,
# and repeats this. Our social science student now records pairs of data: the angle of each turn, and the number
# of steps taken after the turn. Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43, 12)].
# Use a turtle to draw the path taken by our drunk friend.

import turtle

window = turtle.Screen()
tess = turtle.Turtle()
tess.pensize(2)

experimental_data = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for angle, steps in experimental_data:
	tess.right(angle)
	tess.forward(steps)

window.mainloop()
