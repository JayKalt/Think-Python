# Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon. When called
# with draw_poly(tess, 8, 50), it will draw a shape like this:

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

def draw_poly(t, n, sz):
	"""
	  Draws a polygon with the given turtle, number of sides and
	  length of each side.
	  Void function
	"""

	angle = 360 / n

	for _ in range(n):
		t.forward(sz)
		t.left(angle)

window = make_window("lightgreen", "ex3.py")
tess = make_turtle("hotpink", 3)

draw_poly(tess, 8, 60)

window.mainloop()
