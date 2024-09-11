# Draw this pretty pattern.

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

window = make_window("lightgreen", "ex4.py")
tess = make_turtle("blue", 3)

for _ in range(20):
	draw_poly(tess, 4, 100)
	tess.left(360 / 20)

window.mainloop()
