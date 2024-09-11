# Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units,
# turn right by 144, put the pen down, and draw the next star. You’ll get something like this:

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


window = make_window("darkblue", "good_night")
tess = make_turtle("yellow", 3)

for _ in range(5):
	tess.penup()
	tess.fd(350)
	tess.rt(144)
	tess.pendown()
	draw_star(tess)

window.mainloop()
