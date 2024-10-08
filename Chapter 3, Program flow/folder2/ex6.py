# A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another
# 100 steps, turns another random amount, etc.
# A social science student records the angle of each turn before the next 100 steps are taken.
# Her experimental data is [160, -43, 270, -97, -43, 200, -940, 17, -86]. (Positive angles are counter-clockwise.)

# Use a turtle to draw the path taken by our drunk friend.

import turtle

window = turtle.Screen()
tess = turtle.Turtle()
tess.pensize(5)

experimental_data = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for angle in experimental_data:
	tess.right(angle)
	tess.forward(100)

window.mainloop()
