# Write a void function to draw a star, where the length of each side is 100 units.
# (Hint: You should turn the turtle by 144 degrees at each point.)

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

def draw_star(t):
	"""
	  Draw a star where the lenght of each side is 100 units
	  Void function
	"""

	for _ in range(5):
		t.fd(100)
		t.rt(144)


window = make_window("white", "ex9.py")
tess = make_turtle("black", 3)

draw_star(tess)

window.mainloop()
