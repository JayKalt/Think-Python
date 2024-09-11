# Write a void function draw_equitriangle(t, sz) which calls draw_poly from the previous question
# to have its turtle draw a equilateral triangle.

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
	  Draw a polygon with the given turtle, number of sides and
	  length of each side.
	  Void function
	"""

	angle = 360 / n

	for _ in range(n):
		t.fd(sz)
		t.lt(angle)

def draw_equitriangle(t, sz):
	"""
	  Draw a equilateral triangle with the given turtle, and size
	  using draw_poly function
	  Void function
	"""
	draw_poly(t, 3, sz)


window = make_window("lightgreen", "ex6.py")
tess = make_turtle("blue", 3)

draw_equitriangle(tess, 100)
window.mainloop()
