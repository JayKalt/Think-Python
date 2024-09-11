# Write a program to draw this. Assume the innermost square is 20 units per side, and each successive square is
# 20 units bigger, per side, than the one inside it.

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

def set_bigger(space, turtle):
	"""
	  Takes the space needed to create a bigger square and the turtle.
	  Void function
	"""

	turtle.penup()
	turtle.backward(space / 2)
	turtle.right(90)
	turtle.forward(space / 2)
	turtle.left(90)
	turtle.pendown()


window = make_window("lightgreen", "ex2.py")
tess = make_turtle("hotpink", 3)
size = 20

for _ in range(5):
	draw_square(size, tess)
	set_bigger(20, tess)
	size += 20


window.mainloop()
