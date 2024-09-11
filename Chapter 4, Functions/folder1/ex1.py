# Write a void (non-fruitful) function to draw a square. Use it in a program to draw the image shown below.
# Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the
# last square when the program ends.)

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

def draw_square(side, turtle):
	"""
	  Takes the length of a side and the turtle, then draws a square.
	  Void function
	"""

	for _ in range(4):
		turtle.forward(side)
		turtle.left(90)


window = make_window("lightgreen", "ex1.py")
tess = make_turtle("hotpink", 3)

for _ in range(5):
	draw_square(20, tess)
	turtle.penup()
	turtle.forward(40)
	turtle.pendown()

window.mainloop()
