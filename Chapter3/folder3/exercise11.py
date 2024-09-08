# Many interesting shapes can be drawn by the turtle by giving a list of pairs like we did above, where the first
# item of the pair is the angle to turn, and the second item is the distance to move forward. Set up a list of pairs so
# that the turtle draws a house with a cross through the centre, as show here. This should be done without going
# over any of the lines / edges more than once, and without lifting your pen.

import turtle

window = turtle.Screen()

tess = turtle.Turtle()
tess.pensize(10)
tess.hideturtle()

instr = [(270, 100), (30, 100), (120, 100), (120, 100), (225, 140), (135, 100), (135, 140), (135, 100)]

for angle, line in instr:
	tess.right(angle)
	tess.forward(line)

window.mainloop()
