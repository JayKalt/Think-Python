# The two spirals in this picture differ only by the turn angle. Draw both.

import turtle

def make_window(color, title):
	"""
	  Set up the window with the given background color and title.
	  Returns the new window.
	"""

	window = turtle.Screen()
	window.title(title)
	window.bgcolor(color)
	return window

def make_turtle(color, size):
	"""
	  Set up a turtle with the given background color and title.
	  Returns the new window.
	"""

	animal = turtle.Turtle()
	animal.color(color)
	animal.pensize(size)
	return animal

def spiral(turtle, spirals, angle, size, s_inc):
	"""
	  Draw a spiral with the given parametrs:
		turtle  : the turtle
		spirals : number of spirals
		angle   : starting angle
		size    : starting size
		s_inc   : size increment

	  Void function
	"""
	turtle.right(90)
	for _ in range(spirals):
		for _ in range(4):
			turtle.forward(size)
			size += s_inc
			turtle.right(angle)


window = make_window("lightgreen", "ex5.py")
tess = make_turtle("blue", 2)

#spiral(tess, 24, 90, 2, 2.5)
#spiral(tess, 24, 89, 2, 2.5)

window.mainloop()
